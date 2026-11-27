# Guía para construir la célula por etapas

El objetivo es recuperar el trabajo de Gym Tracker y CEDEAR Tracker y convertirlo en una forma de trabajo reusable. La implementación será incremental: cada sesión deja evidencia y un próximo paso preciso.

## Paso 0 Abrir el repo y comprobar continuidad

Abrir la carpeta de este repositorio como proyecto propio en Codex. Leer README, STATUS y ROADMAP. Ejecutar `python3 scripts/check_state.py`. Revisar `git status --short` y el último commit antes de modificar archivos. No tratar el repositorio padre de Documents/Codex como este proyecto.

E00 ya contiene las bases. Los siguientes pasos se ejecutan en futuras sesiones según el alcance solicitado.

## Paso 1 Consolidar el contexto del piloto

Elegir un tracker e identificar su repo. Recopilar instrucciones de Claude o ChatGPT, `CLAUDE.md`, `AGENTS.md`, decisiones, comandos, modelos de datos y problemas recurrentes. Importar extractos útiles con referencia y fecha; mantener exportaciones crudas privadas fuera de Git.

Usar templates/PROJECT_CONTEXT.md para describir cliente, problema, etapa, stack, comandos y operación. Crear en el piloto `docs/project-context.md` y `docs/constraints.md`. Cada constraint incluye ID, regla, motivo, alcance, fuente y forma de verificarlo. Distinguir regla obligatoria de preferencia y supuesto.

Contrastar documentación con código, tests y despliegue. No convertir una conversación antigua en regla vigente automáticamente. Reutilizar instrucciones válidas; registrar contradicciones antes de sustituirlas.

Salida E01: contexto consolidado, fuente de cada regla, incógnitas visibles y un cambio pequeño elegido para el piloto.

Prompt:

> Ejecutá E01 sobre el repo que te indiqué. Revisá las instrucciones existentes y los materiales aportados. Consolidá contexto y constraints con evidencia. Separá método reusable de decisiones del producto. Registrá contradicciones y actualizá el avance del repositorio product-cell.

## Paso 2 Instalar los roles y el procedimiento

Primero revisar las instrucciones vigentes del piloto. Integrar las reglas de continuidad sin sobrescribirlas. Crear agentes personalizados desde las plantillas de templates/agents, ajustando modelos disponibles y contratos al proyecto. Copiarlos a `.codex/agents/` del piloto solo en esta etapa.

Usar skill-creator para crear `.agents/skills/product-cell/SKILL.md` y cuatro referencias de modo. El cuerpo principal solo clasifica, consulta estado, carga la referencia pertinente y coordina. Las referencias contienen los recorridos de WORKFLOWS. Mantener el contexto específico del producto fuera de la skill reusable.

El coordinador debe leer el estado antes de asignar trabajo. Cada pedido delegado incluye ID de tarea, modo, etapa de producto, estado, aceptación, archivos relevantes, límite de edición y formato de salida. Las restricciones relevantes se leen directamente, nunca se dejan libradas a recuperación semántica.

Configurar el modelo principal en el cliente o configuración admitida. Verificar disponibilidad antes de fijar IDs de modelos. Las plantillas no alteran permisos del entorno; producción requiere herramientas y credenciales apropiadas al alcance autorizado.

Prueba en seco: abrir una sesión nueva, pedir que identifique instrucciones, skill, agentes, etapa actual y próximo paso. Hacer una delegación inocua y acotada para comprobar carga y salida. Registrar lo observado; no inferir el modelo realmente ejecutado solo por el contenido del archivo.

Salida E02: configuración detectada y handoff de ejemplo comprobado. No es todavía evidencia de éxito en tareas reales.

## Paso 3 Probar tweak y bugfix con presupuesto acotado

Crear una tarea con templates/TASK.md para un tweak real. Definir aceptación breve, riesgo y verificaciones. El coordinador puede resolver lo trivial o delegar al dev económico si aporta valor. No exigir PM y Tech Lead en un cambio inequívoco.

Luego elegir un bug real. Registrar comportamiento esperado, reproducción, diagnóstico, corrección y verificación de regresión. Completar templates/LEARNING.md con prevención accionable. Si no se consigue reproducir, indicar la evidencia disponible y lo no confirmado; no inventar una causa.

Registrar métricas usando templates/METRICS.csv: rondas, reintentos, defecto encontrado en revisión, tiempo y consumo cuando sea observable. Un dato no disponible queda vacío, no en cero. Comparar el costo total hasta aceptación, no solo la primera respuesta del modelo económico.

Salida E03: dos tareas verificadas y un learning útil; ajustar arneses según los fallos observados.

## Paso 4 Probar una etapa de roadmap

El PM define un resultado, métrica, alcance y exclusiones de etapa. El Tech Lead evalúa viabilidad y dependencias. Descomponer en historias verticales verificables, evitando refinar todo el backlog.

Seleccionar una historia: PM define flujo, estados y aceptación; Tech Lead produce contratos, impacto y plan de pruebas; PM revisa efectos sobre la experiencia. Máximo inicial de dos rondas antes de elevar desacuerdos con alternativas. Una decisión bloqueante impide el pase a Dev.

El Dev implementa la spec versionada. Reviewer revisa diff, evidencia y aceptación. El PM interviene en aceptación cuando existe decisión de experiencia; no repetir revisión funcional completa para cambios sin impacto. DevOps participa antes si hay migraciones o infraestructura.

Salida E04: una historia de principio a fin con evidencia de aceptación, entrega y próximos resultados a medir. Revisar WORKFLOWS si se descubre que el problema requería discovery fundacional.

## Paso 5 Hacer reproducible la entrega

Identificar el pipeline y el entorno del piloto. Documentar comandos, variables requeridas sin sus valores secretos, migraciones, chequeos de salud, observabilidad y rollback. Conectar los checks que ya usa el repo; agregar únicamente verificaciones que cubran riesgos reales.

Establecer qué acciones están autorizadas y cuáles necesitan una decisión adicional. Preparar un cambio revisable antes de pedir una aprobación final que sea necesaria. Una spec aprobada no sustituye los permisos técnicos de producción.

Probar despliegue y rollback en un entorno adecuado. Registrar qué se probó y qué solo se documentó. Para mantenimiento continuo, definir disparador concreto, alcance, acceso a logs y responsable. No asumir que un chat cerrado mantiene vigilancia permanente.

Salida E05: entrega repetible y recuperación comprobada en el entorno registrado.

## Paso 6 Crear la biblioteca antes del RAG

Curar decisiones, learnings, runbooks y extractos de conversaciones. Mantener fuentes, fechas y estado de vigencia. Separar corpus por proyecto y marcar explícitamente los patrones transferibles.

Comenzar con `rg` y un índice humano. Preparar entre 10 y 20 preguntas reales con fuentes esperadas: por qué se decidió algo, cómo se resolvió un bug o dónde está una restricción. Medir si se encuentran fuentes correctas y cuánto contexto hace falta.

Salida E06: búsqueda textual útil y casos concretos que justifiquen, o no, recuperación semántica.

## Paso 7 Evaluar RAG local

Seguir docs/RAG.md. Elegir embeddings y almacenamiento recién al conocer tamaño, privacidad, latencia y disponibilidad del entorno. Indexar incrementalmente, conservar referencias y eliminar contenido borrado o sustituido.

Comparar recuperación híbrida con la línea base textual sobre las mismas preguntas. Probar filtros entre proyectos, documentos obsoletos y contenido que intente dar instrucciones. La tarea activa y la spec nunca dependen de top-k semántico.

Salida E07: decisión documentada de adoptar, ajustar o postergar RAG basada en calidad, costo y mantenimiento. Si se adopta, integrar la consulta mediante una herramienta invocable y registrar corpus, filtros y evidencia devuelta.

## Paso 8 Llevar el método al segundo tracker

Extraer skills y roles que resultaron estables. Mantener constraints, modelos de dominio, comandos y credenciales separados por proyecto. Registrar la versión del método instalada en cada repo.

Probar una tarea real en el segundo tracker. Verificar que no recibe reglas ni antecedentes privados del primero sin pertinencia y autorización. Ajustar solo con evidencia; no crear un plugin distribuible antes de estabilizar la interfaz del método.

## Protocolo de cierre en todas las etapas

Actualizar tarea, STATUS, state/project.json, ROADMAP y LOG. Guardar decisiones duraderas. Correr el verificador y revisar el diff. El cierre informa último paso completo, trabajo parcial, evidencia, impedimentos y próxima acción concreta. Crear un commit del alcance terminado cuando corresponda, sin incluir archivos ajenos ni secretos.
