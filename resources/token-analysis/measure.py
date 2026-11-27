"""Static source counts, NOT runtime usage. Requires tiktoken 0.14.0.
Usage: python measure.py /path/to/spec-kit /path/to/bmad /output/directory
Expected tags: Spec Kit v1.4.5, BMAD v6.12.4.
"""
import csv,json,sys
from pathlib import Path
import tiktoken
enc=tiktoken.get_encoding('o200k_base')
spec,bmad,out=map(Path,sys.argv[1:4]);out.mkdir(parents=True,exist_ok=True)
paths=[]
for p in sorted((spec/'templates/commands').glob('*.md')): paths.append(('spec-kit',spec,p))
for p in sorted((spec/'templates').glob('*template.md')): paths.append(('spec-kit',spec,p))
for ext in ['bug','assess']:
    for p in sorted((spec/f'extensions/{ext}/commands').glob('*.md')): paths.append(('spec-kit',spec,p))
for p in sorted((bmad/'src/bmm-skills/ship/bmad-build').rglob('*.md')): paths.append(('bmad',bmad,p))
rows=[]
for framework,root,p in paths:
    content=p.read_text()
    rows.append(dict(framework=framework,path=str(p.relative_to(root)),characters=len(content),tokens_o200k_base=len(enc.encode(content))))
with (out/'source-counts.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
lookup={(r['framework'],r['path']):r['tokens_o200k_base'] for r in rows}
bprefix='src/bmm-skills/ship/bmad-build/'
groups={
'spec_sdd_core_commands':[('spec-kit',f'templates/commands/{n}.md') for n in ['specify','plan','tasks','implement','converge']],
'spec_optional_clarify_analyze':[('spec-kit',f'templates/commands/{n}.md') for n in ['clarify','analyze']],
'spec_bug_commands':[('spec-kit',f'extensions/bug/commands/speckit.bug.{n}.md') for n in ['assess','fix','test']],
'spec_assess_commands':[('spec-kit',f'extensions/assess/commands/speckit.assess.{n}.md') for n in ['intake','research','shape','define','decide']],
'bmad_dispatch_parent_source':[('bmad',bprefix+n) for n in ['SKILL.md','workflow.md','step-01-clarify-and-route.md','step-02-plan.md','spec-template.md','step-03-implement.md','step-04-review.md','step-05-present.md']],
'bmad_oneshot_parent_source':[('bmad',bprefix+n) for n in ['SKILL.md','workflow.md','step-01-clarify-and-route.md','step-02-plan.md','spec-template.md','step-oneshot.md']],
'bmad_two_reviewer_instruction_files':[('bmad',bprefix+'review-prompts/'+n+'.md') for n in ['edge-case-hunter','verification-gap']]
}
result={k:dict(tokens=sum(lookup[p] for p in group),files=[p[1] for p in group]) for k,group in groups.items()}
(out/'groups.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
print('\nPER FILE:')
for r in rows:print(r['tokens_o200k_base'],r['framework'],r['path'])
