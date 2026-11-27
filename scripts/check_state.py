#!/usr/bin/env python3
"""Validate documentation links and the construction state, not agent execution."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

try:
    state = json.loads((ROOT / 'state/project.json').read_text())
except (OSError, ValueError) as exc:
    print(f'FAIL: Cannot read project state: {exc}')
    sys.exit(1)

stages = {f'E{i:02d}' for i in range(9)}
require(state.get('schema_version') == 1, 'Unsupported state schema')
require(state.get('current_stage') in stages, 'Invalid current stage')
require(state.get('current_stage_status') in {'not_started', 'in_progress', 'blocked', 'complete'}, 'Invalid stage status')
require(state.get('mode') in {'foundation', 'roadmap_stage', 'tweak', 'bugfix'}, 'Invalid mode')
completed = state.get('completed_stages', [])
require(isinstance(completed, list), 'completed_stages must be a list')
if not isinstance(completed, list):
    completed = []
require(all(s in stages for s in completed), 'Unknown completed stage')
require(len(completed) == len(set(completed)), 'Duplicate completed stages')
require(state.get('last_completed_stage') in completed, 'Last completed stage absent from completed stages')
require(bool(state.get('next_action')), 'Missing next action')
if state.get('current_stage_status') != 'complete':
    require(state.get('current_stage') not in completed, 'Incomplete current stage listed as complete')
else:
    require(state.get('current_stage') in completed, 'Complete current stage missing from completed stages')
for target in state.get('evidence', []):
    require((ROOT / target).is_file(), f'Missing evidence file: {target}')
if state.get('active_task'):
    require((ROOT / state['active_task']).is_file(), 'Missing active task file')

roadmap = (ROOT / 'docs/ROADMAP.md').read_text()
checked = set(re.findall(r'^- \[x\] (E\d{2})', roadmap, re.M))
require(checked == set(completed), 'Roadmap checkboxes disagree with structured state')
status = (ROOT / 'docs/STATUS.md').read_text()
require(state['current_stage'] in status, 'Current stage absent from STATUS')
require(state['last_completed_stage'] in status, 'Last completed stage absent from STATUS')

count = 0
for file in ROOT.rglob('*.md'):
    if '.git' in file.parts:
        continue
    count += 1
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', file.read_text()):
        if target.startswith(('https://', 'http://', '#', 'mailto:')):
            continue
        path = target.split('#', 1)[0]
        if path:
            require((file.parent / path).exists(), f'Broken link in {file.relative_to(ROOT)}: {target}')

try:
    import tomllib
except ImportError:
    print('NOTE: TOML parsing skipped; Python 3.11+ is needed for that additional check.')
else:
    for file in (ROOT / 'templates/agents').glob('*.toml'):
        try:
            data = tomllib.loads(file.read_text())
            for key in ('name', 'description', 'developer_instructions', 'model', 'model_reasoning_effort'):
                require(bool(data.get(key)), f'{file.name}: missing {key}')
        except ValueError as exc:
            errors.append(f'Invalid TOML {file.name}: {exc}')

if errors:
    print('\n'.join(f'FAIL: {error}' for error in errors))
    sys.exit(1)
print(f'OK: state, roadmap and links in {count} Markdown files. This does not validate runtime capabilities.')
