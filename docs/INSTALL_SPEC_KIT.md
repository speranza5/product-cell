# Instalación gradual de Spec Kit con Codex

Esta guía se ejecuta en E02, después de elegir el tracker y completar E01. Adaptar la célula no significa que Spec Kit ya esté instalado. Los comandos se contrastaron con el código y las guías de v1.4.5; aún no se ejecutaron en un tracker.

## 1 Comprobar entorno y destino

Abrir una terminal en la raíz del repo piloto. Confirmar ruta antes de inicializar; no ejecutar init en product-cell por accidente.

```sh
pwd
git rev-parse --show-toplevel
git status --short
command -v uv
uv --version
command -v codex
codex --version
python3 --version
```

Se requiere Python 3.11 o superior y uv para la ruta propuesta. La integración documentada usa Codex CLI; verificar su disponibilidad aunque se trabaje desde la app. Si uv no está instalado, usar las [instrucciones oficiales](https://docs.astral.sh/uv/getting-started/installation/); en macOS con Homebrew ya disponible puede usarse `brew install uv`. No sustituir el Python del sistema: `uv python install 3.11` permite preparar un intérprete gestionado si hace falta.

En la sesión de creación del repo, el Python por defecto no incluía tomllib y uv no estaba en PATH. Volver a comprobar: esto no describe necesariamente el entorno futuro.

## 2 Fijar versión y comprobar el CLI

Para el piloto usar una ejecución aislada y versionada; no reemplaza un specify instalado globalmente:

```sh
uvx --python 3.11 --from git+https://github.com/github/spec-kit.git@v1.4.5 specify version
uvx --python 3.11 --from git+https://github.com/github/spec-kit.git@v1.4.5 specify init --help
```

Registrar la salida de versión, el origen y la versión de Codex. En esta release el scaffolding proviene de assets incluidos con el CLI. Si se adopta otra release, volver a verificar sintaxis, defaults y mediciones.

Alternativa persistente, después de validar el piloto:

```sh
uv tool install --python 3.11 specify-cli --from git+https://github.com/github/spec-kit.git@v1.4.5
specify version
```

Elegir una ruta y evitar invocar por error otra versión que esté antes en PATH. No usar upgrades automáticos durante la medición.

## 3 Preparar un cambio revisable

Resolver o preservar cambios locales del usuario antes de inicializar. Crear una rama desde una base conocida:

```sh
git switch -c codex/adopt-spec-kit
```

Si ya existe, inspeccionarla o usar otro nombre; no borrarla. Registrar el commit de base. Revisar conflictos potenciales en `.specify/`, `.agents/skills/` y `.codex/config.toml`. Si el repo ya usa Spec Kit, seguir su guía de upgrade/integración en lugar de reinicializar ciegamente.

## 4 Inicializar core con Codex

Desde la raíz confirmada del tracker, con una base revisable:

```sh
uvx --python 3.11 --from git+https://github.com/github/spec-kit.git@v1.4.5 specify init --here --force --non-interactive --integration codex --script sh --events false
```

`--force` permite fusionar en una carpeta no vacía y puede reemplazar rutas administradas en conflicto; por eso primero se inspecciona la base. `--events false` mantiene los handlers de eventos de Spec Kit desactivados para el primer piloto. No desactiva las instrucciones/hooks de una extensión que se instale posteriormente.

Revisar archivos nuevos además del diff de archivos conocidos:

```sh
git status --short
git diff --stat
git diff -- .codex/config.toml
rg --files --hidden .specify .agents/skills
```

Comprobar que aparecen skills `speckit-*`. No instalar automáticamente extensiones de Git/GitHub, catálogos comunitarios, RAG ni bundles. Ya tenemos Git y herramientas del entorno para el ciclo inicial.

## 5 Integrar reglas y fuentes canónicas

En un chat de Codex dentro del piloto, ejecutar una skill por vez. Son prompts de chat, no comandos shell:

```text
$speckit-constitution Consolidá las reglas ya verificadas en E01.
Usá docs/constraints.md y sus fuentes. No inventes estándares.
Registrá las reglas acordadas en .specify/memory/constitution.md.
```

Revisar el resultado antes de desarrollar. Mantener AGENTS.md operativo y breve; referenciar constitución y estado. El inventario de constraints pasa a enlazar las reglas canónicas para evitar copias divergentes. Consultar [SPEC_KIT.md](SPEC_KIT.md) para la asignación de documentos.

Integrar [el fragmento de instrucciones](../templates/PILOT_AGENTS_FRAGMENT.md) sin sobrescribir instrucciones existentes. Instalar solo los agentes personalizados necesarios desde `templates/agents/`, ajustando modelo y esfuerzo disponibles. Su instalación no demuestra que fueron ejecutados.

## 6 Probar un tweak y habilitar bugs cuando haga falta

Primero un tweak: ticket corto con aceptación y evidencia, sin invocar SDD completo. Para el bug de E03 que justifique el proceso estructurado:

```sh
uvx --python 3.11 --from git+https://github.com/github/spec-kit.git@v1.4.5 specify extension add bug
uvx --python 3.11 --from git+https://github.com/github/spec-kit.git@v1.4.5 specify extension list
```

Registrar versión/origen efectivo de la extensión; no asumir que cualquier componente comparte el número de versión del CLI. Inspeccionar sus skills y hooks instalados. En el chat, por separado y revisando cada salida:

```text
$speckit-bug-assess Descripción, reproducción y resultado esperado. slug=mi-bug
$speckit-bug-fix slug=mi-bug
$speckit-bug-test slug=mi-bug
```

Los tres artefactos se conservan en `.specify/bugs/mi-bug/`. No sustituir la prueba del fallo original por una suite que no lo cubre. Registrar learning como prevención y enlace al caso; evitar un cuarto informe que repita los anteriores.

## 7 Usar SDD para una historia acotada

En E04, una skill por vez:

```text
$speckit-specify Describí la funcionalidad y sus límites ya acordados.
$speckit-plan Reutilizá arquitectura y constraints del repo.
$speckit-tasks Descomponé la feature en tareas cohesionadas y verificables.
$speckit-implement Ejecutá únicamente las tareas seleccionadas; indicá sus IDs reales.
$speckit-converge Contrastá implementación y artefactos vigentes.
```

Usar clarify antes de plan si hay ambigüedad y analyze antes de implementar cuando complejidad/riesgo lo justifiquen, o si un gate configurado lo exige. No inventar IDs: leer tasks.md. No ejecutar todo el roadmap por invocar implement. Converge puede descubrir tareas; no iniciar un bucle ilimitado: aplicar la política de escalamiento con evidencia.

## 8 Incorporar discovery estructurado solo cuando corresponda

Para una idea nueva que necesite evaluación estructurada:

```sh
uvx --python 3.11 --from git+https://github.com/github/spec-kit.git@v1.4.5 specify extension add assess
```

Orden: `$speckit-assess-intake`, `$speckit-assess-research`, `$speckit-assess-define`, `$speckit-assess-shape`, `$speckit-assess-decide`, con el mismo slug y una invocación por paso. Incorporar las cinco preguntas y el ICP en los artefactos pertinentes, sin duplicar un dossier paralelo. El resultado go no inicia implementación automáticamente. No regenerar todos los pasos cuando cambia un dato; revisar artefactos dependientes.

## 9 Comprobar continuidad y registrar instalación

Completar [INSTALLATION_RECORD.md](../templates/INSTALLATION_RECORD.md) en el piloto. Abrir un chat nuevo y pedir:

> Identificá el modo, la etapa de producto, la tarea activa, su fuente canónica y el siguiente paso. Indicá qué skills y agentes están disponibles y qué falta verificar. No implementes nada todavía.

E02 se completa cuando core, configuración y handoff se verifican. E03/E04 demuestran ejecución real y consumo. Registrar modelo observado y telemetría disponible; un campo de configuración no es evidencia de ejecución.

## 10 Actualizar o revertir

Conservar commit de adopción y lista de archivos generados. Una actualización va en rama propia, con nueva versión fijada, revisión del diff y una tarea pequeña de regresión. Mantener customizaciones mediante overrides/presets soportados, no editando skills generadas.

Para revertir, deshacer únicamente los commits y archivos de adopción identificados, preservando cambios posteriores del usuario. No usar `git reset --hard` ni borrar `.agents` o `.codex` completas. La ejecución uvx no deja una instalación persistente en PATH; su caché no necesita borrarse para revertir archivos del proyecto.

## Referencias de la versión

- [Instalación](https://github.com/github/spec-kit/blob/v1.4.5/docs/installation.md)
- [Codex](https://github.com/github/spec-kit/blob/v1.4.5/docs/integrations/codex.md)
- [Repos existentes](https://github.com/github/spec-kit/blob/v1.4.5/docs/how-to/existing-projects.md)
- [Bugs](https://github.com/github/spec-kit/blob/v1.4.5/docs/guides/bugfix.md)
- [Assessment](https://github.com/github/spec-kit/blob/v1.4.5/docs/guides/assessment.md)
