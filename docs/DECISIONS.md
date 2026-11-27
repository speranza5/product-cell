# Registro de decisiones

Fecha inicial: 2026-11-27. Decisiones de diseño acordadas en esta conversación; su eficacia se valida por etapas. Para sustituir una decisión, conservarla con estado superseded y enlazar su reemplazo.

| ID | Decisión | Motivo y consecuencia | Estado |
|---|---|---|---|
| D01 | Un coordinador y cinco roles bajo demanda | Estado coherente y menor coordinación innecesaria | Aceptada |
| D02 | Cuatro modos y riesgo separado | Adecuar procedimiento al tipo e impacto del trabajo | Aceptada |
| D03 | Estado en Git, independiente del chat | Retomar a lo largo del tiempo con evidencia | Aceptada |
| D04 | PM protege aceptación y Tech Lead constraints | Evitar cambios funcionales accidentales durante implementación | Aceptada |
| D05 | Modelo económico para tareas cerradas | Evaluar ahorro total incluyendo reintentos | Propuesta para piloto |
| D06 | Una skill con referencias por modo al inicio | Reducir superficie y cargar solo procedimiento pertinente | Propuesta para E02 |
| D07 | RAG después de búsqueda textual | Justificar complejidad con problemas reales de recuperación | Aceptada |
| D08 | Spec, estado y restricciones por lectura directa | No depender de recall semántico para obligaciones | Aceptada |
| D09 | Learning proporcional y accionable | Evitar acumulación de reglas sin utilidad | Aceptada |
| D10 | Repo Git local independiente | No mezclar este trabajo con el repo padre ni publicar sin destino | Implementada |
| D11 | Markdown como documentación inicial | Edición y diffs simples junto al estado y plantillas | Implementada |

## Pendientes

- Elegir tracker y ruta del piloto.
- Confirmar variante de las cinco preguntas.
- Validar modelos y esfuerzo disponibles en el cliente.
- Establecer entornos, pipeline y permisos del piloto.
- Elegir procesamiento local o externo para embeddings si E07 se justifica.
- Definir remoto Git solo cuando exista un destino solicitado.
