# Spec Kit como base de la célula

Decisión del 27 de noviembre de 2026: adoptar Spec Kit como base del piloto, con configuración selectiva. No se ha demostrado un ahorro de tokens frente a BMAD. La aceptación operativa depende del piloto y de la calidad obtenida por consumo total.

## Responsabilidades sin duplicación

| Capa | Responsabilidad |
|---|---|
| Spec Kit | Procesos, specs, planes, tareas y evidencias de sus extensiones |
| product-cell | Clasificación de los cuatro modos, asignación de roles, política de consumo y continuidad |
| Codex | Ejecución, herramientas, modelos y subagentes disponibles |
| Repo y CI del piloto | Código, verificaciones ejecutables y entrega |
| Biblioteca local, luego RAG si conviene | Antecedentes recuperables con procedencia |

Este repo conserva el roadmap de construcción del método. El tracker conserva su roadmap de producto. No generar una segunda spec funcional o lista de tareas en product-cell para un cambio que ya gestiona Spec Kit.

## Fuentes canónicas en el piloto

| Información | Fuente |
|---|---|
| Principios técnicos obligatorios | `.specify/memory/constitution.md`, consolidada desde reglas existentes |
| Instrucciones operativas del agente | `AGENTS.md`, breve y con referencias |
| Contexto de producto | `docs/project-context.md` |
| Specs de una funcionalidad | `spec.md`, `plan.md`, `tasks.md` en la carpeta de feature que resuelva Spec Kit |
| Diagnóstico y verificación de bug con extensión | `.specify/bugs/<slug>/assessment.md`, `fix.md`, `test.md` |
| Evaluación fundacional con extensión | `.specify/assessments/<slug>/` |
| Tweak o bug trivial sin extensión | Un ticket breve con aceptación y evidencia |
| Enrutamiento y próximo paso | Índice compacto con referencias a los anteriores |
| Learning | Prevención en test, runbook o decisión; índice con enlace al caso |

`docs/constraints.md` de E01 es el inventario de migración con fuentes. En E02 consolidar las reglas aceptadas en la constitución y reemplazar texto duplicado por referencias. Reglas específicas por directorio pueden seguir en AGENTS.md locales; explicitar alcance y resolver contradicciones. No reescribir automáticamente normas vigentes del repo.

## Mapa de modos

| Modo | Recorrido mínimo | Escalamiento |
|---|---|---|
| Fundacional | PM usa evidencia y las cinco preguntas; ICP y decisión compactos | Si necesita investigación estructurada, extensión assess: intake → research → define → shape → decide |
| Etapa de roadmap | Objetivo de etapa; una feature acotada: specify → plan → tasks → implement → converge | clarify ante ambigüedad; analyze para consistencia cuando la complejidad/riesgo lo justifique |
| Tweak | Ticket breve → ejecución directa o dev → comprobación proporcional | Si afecta contratos, datos o decisiones de experiencia, reclasificar |
| Bugfix | Reproducción y causa → corrección → regresión → learning | Para diagnóstico incierto o impacto relevante, extensión bug: assess → fix → test |

No saltar prerequisitos dentro de un proceso invocado. El modo ligero es una decisión de ruta antes de invocar Spec Kit, no una orden de ignorar sus checks. Un gate obligatorio instalado permanece obligatorio hasta que su política se cambie explícitamente.

## Roles y subagentes

PM opera sobre los artefactos funcionales canónicos; Tech Lead sobre plan y decisiones técnicas; Dev ejecuta tareas listas; Reviewer revisa diff y aceptación; DevOps actúa cuando hay trabajo operativo. Los roles no necesitan una sesión separada siempre.

Una invocación de skill Spec Kit no crea por sí sola nuestra célula. El coordinador decide la delegación explícita y evita repetir el proceso dentro de cada subagente. El dev recibe tareas concretas y referencias; no vuelve a ejecutar specify o plan para una historia ya refinada.

Para una implementación larga, acotar cada invocación a tareas o una fase. Cambiar de sesión con un handoff pequeño cuando sea necesario. Evitar un subagente por microtarea si el costo de arranque domina; agrupar cambios cohesivos. No usar el tamaño de ventana como presupuesto de tokens: limitar contexto no establece un tope de consumo agregado.

## Cambios y actualizaciones

Referencia inicial: Spec Kit v1.4.5, commit `6ba8beefff8d6408cadd62038e92d459093e33a8`. Registrar versión del CLI, integración, extensiones y modelos observados. Usar overrides/presets para cambios de plantilla y extensiones para capacidades nuevas; no editar archivos generados esperando que sobrevivan una actualización.

En E02 empezar con core y un AGENTS.md conciso. Crear una skill de enrutamiento solo si se necesita un procedimiento reusable; no crear otro motor de workflow. Empaquetar un preset o bundle propio en E08, después de validar el piloto. No instalar BMAD junto a Spec Kit como segundo orquestador; queda como referencia comparativa.

## Criterio de aceptación

El piloto debe retomar una tarea sin reconstruir el chat, respetar constraints, entregar cambios aceptados y registrar consumo observable de coordinador y subagentes. No atribuir ahorro a una versión o framework por el tamaño de sus archivos fuente.

Ver [instalación](INSTALL_SPEC_KIT.md), [política de tokens](TOKEN_POLICY.md) y [evidencia estática](../resources/token-analysis/METODOLOGIA.md).
