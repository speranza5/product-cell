# Recorridos según el trabajo

Implementación de estos recorridos: [Spec Kit y fuentes canónicas](SPEC_KIT.md). Usar ese mapa para decidir qué skill invocar; no todas las solicitudes necesitan un proceso completo.

## Clasificación

El coordinador distingue modo, etapa de producto y estado de tarea. Clasifica con la información disponible y pregunta solo cuando la ambigüedad cambia intención o alcance. Registrar reclasificaciones y su motivo. El riesgo se evalúa por impacto en datos, permisos, contratos, experiencia y operación; no por cantidad de líneas cambiadas.

## Fundacional

Entrada: idea, evidencia disponible y restricciones conocidas. PM conduce cinco preguntas propuestas de Working Backwards: quién es el cliente, qué problema tiene, cuál es el beneficio principal, cómo sabemos lo que necesita y cómo sería la experiencia. Confirmar esta variante con el usuario al importar su método.

Salida: brief, ICP hipotético, alcance inicial, experimento y roadmap. ICP incluye contexto, objetivo, frecuencia/severidad del problema, alternativa actual, disparador, usuario/comprador y exclusiones. Separar hechos, hipótesis y preguntas. La aprobación de una idea no demuestra validación de mercado.

Tech Lead participa para viabilidad con impacto en la propuesta. El usuario decide la apuesta de producto. La primera etapa acordada continúa por roadmap_stage. Se reutiliza contexto vigente si el cambio fundacional afecta solo una parte.

## Etapa de roadmap

Entrada: producto definido, aprendizajes previos y resultado deseado. PM define objetivo, métrica, alcance y condición de salida. Tech Lead evalúa dependencias y riesgos. Breakdown en historias con valor verificable; detalle solo para trabajo próximo.

Historia lista: aceptación observable, reglas y estados relevantes, exclusiones, contratos técnicos cuando correspondan, constraints identificados, pruebas proporcionales y ninguna decisión bloqueante. PM y Tech Lead refinan hasta dos rondas iniciales; los desacuerdos pendientes vuelven con opciones y recomendación.

Dev implementa, Reviewer comprueba, DevOps entrega si corresponde. Una etapa distingue salida desplegada de resultado observado; si la métrica necesita tiempo, registrar cuándo se revisará y quién la revisa.

## Tweak

Entrada: comportamiento deseado inequívoco, impacto local y reversible. Ticket breve con qué, dónde, aceptación y verificación. Coordinador → Dev, si delegar aporta valor → comprobación proporcional. PM y Tech Lead no son pasos obligatorios.

Cambios en contratos, permisos, datos o decisiones de experiencia exigen reconsiderar clasificación y profundidad. No usar la etiqueta tweak solo porque el pedido es urgente. Verificación visual puede bastar para texto o layout; la lógica necesita comprobaciones de comportamiento pertinentes.

## Bugfix con learning

Entrada: discrepancia entre resultado esperado y real, con evidencia. Reproducir o acotar la incertidumbre. PM aclara lo esperado si no está definido; Tech Lead entra si el diagnóstico es complejo. Dev corrige y agrega regresión cuando aporta protección. Reviewer comprueba el fallo original y efectos colaterales relevantes.

Un incidente puede requerir mitigación primero. Registrar diagnóstico posterior como pendiente con responsable. El learning cubre disparador, causa confirmada o hipótesis, brecha de detección y prevención. No generar una regla global por cada caso particular.

## Estados y pases

Vocabulario: `triage`, `discovery`, `refinement`, `ready`, `implementation`, `verification`, `ready_for_delivery`, `delivered`, `closed`, `blocked`.

Los modos pueden omitir estados que no aporten. No omitir aceptación ni evidencia. `blocked` conserva el estado previo y la entrada faltante. `delivered` significa entrega comprobada en el entorno indicado; `closed` exige registrar pendientes de observación o prevención con seguimiento.

Un cambio de spec durante desarrollo incrementa su versión e identifica qué implementación y verificaciones deben revisarse. El handoff referencia esa versión y la revisión de código; no se acepta evidencia de una versión incompatible.
