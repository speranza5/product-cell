# Registro de decisiones

Fecha inicial: 2026-11-27. Decisiones de diseño acordadas en esta conversación; su eficacia se valida por etapas. Para sustituir una decisión, conservarla con estado superseded y enlazar su reemplazo.

| ID | Decisión | Motivo y consecuencia | Estado |
|---|---|---|---|
| D01 | Un coordinador y cinco roles bajo demanda | Estado coherente y menor coordinación innecesaria | Aceptada |
| D02 | Cuatro modos y riesgo separado | Adecuar procedimiento al tipo e impacto del trabajo | Aceptada |
| D03 | Estado en Git, independiente del chat | Retomar a lo largo del tiempo con evidencia | Aceptada |
| D04 | PM protege aceptación y Tech Lead constraints | Evitar cambios funcionales accidentales durante implementación | Aceptada |
| D05 | Modelo económico para tareas cerradas | Evaluar ahorro total incluyendo reintentos | Propuesta para piloto |
| D06 | Una skill con referencias por modo al inicio | Antecedente: reemplazado por core Spec Kit y enrutamiento mínimo opcional | Sustituida por D12 y D13 |
| D07 | RAG después de búsqueda textual | Justificar complejidad con problemas reales de recuperación | Aceptada |
| D08 | Spec, estado y restricciones por lectura directa | No depender de recall semántico para obligaciones | Aceptada |
| D09 | Learning proporcional y accionable | Evitar acumulación de reglas sin utilidad | Aceptada |
| D10 | Repo Git local independiente | No mezclar este trabajo con el repo padre ni publicar sin destino | Implementada |
| D11 | Markdown como documentación inicial | Edición y diffs simples junto al estado y plantillas | Implementada |
| D12 | Spec Kit como base del piloto | Adoptar extensibilidad; no presupone ahorro frente a BMAD. v1.4.5 como referencia | Aceptada; instalación pendiente |
| D13 | Una fuente canónica por dato | product-cell enruta; specs/tareas y reportes se mantienen en Spec Kit cuando ese proceso se usa | Aceptada |
| D14 | Revisión proporcional sin cuotas de hallazgos | Evitar fan-out y triage sin justificación de riesgo | Aceptada |
| D15 | Medir consumo hasta aceptación | Incluir coordinador, subagentes, reintentos y calidad; distinguir caché y costo | Aceptada |

## Pendientes

- Elegir tracker y ruta del piloto.
- Confirmar variante de las cinco preguntas.
- Validar modelos y esfuerzo disponibles en el cliente.
- Establecer entornos, pipeline y permisos del piloto.
- Elegir procesamiento local o externo para embeddings si E07 se justifica.
- Remoto resuelto: GitHub privado en speranza5/product-cell, por pedido de publicación del usuario.
