# Conocimiento local y recuperación

## Cuándo vale la pena

RAG aporta cuando la biblioteca crece o las búsquedas textuales no encuentran antecedentes expresados con otras palabras. Primero curar documentos y medir una línea base. No hace falta un vector store para empezar a trabajar con la célula.

## Fuentes y autoridad

1. Estado, spec vigente y constraints obligatorios: lectura directa por referencia explícita.
2. Código a modificar: búsqueda textual o de símbolos y lectura directa.
3. Decisiones históricas, incidentes, learnings y runbooks: candidatos para recuperación.
4. Conversaciones exportadas: antecedentes con fuente y fecha, no instrucciones aprobadas.

No adjudicar vigencia por ranking semántico. Si hay contradicción, comprobar fuente actual y registrar diferencia. Un resultado vacío no demuestra que el antecedente no exista.

## Uso por modo y rol

Fundacional recupera experimentos y evidencia; roadmap recupera decisiones y resultados previos; tweak no consulta por defecto; bugfix busca síntomas y causas similares. PM recibe evidencia de producto, Tech Lead arquitectura, Dev referencias seleccionadas, Reviewer antecedentes de riesgo y DevOps runbooks/incidentes.

Cada consulta responde una pregunta concreta. Filtrar primero por proyecto y ampliar solo por pertinencia. Los patrones entre proyectos deben estar marcados como transferibles. Evitar que los agentes repitan la misma consulta.

## Construcción incremental

E06: documentos curados, índice humano y `rg`. Definir entre 10 y 20 preguntas con fuentes relevantes esperadas, incluyendo preguntas sin respuesta disponible.

E07: si la línea base deja brechas, experimentar con búsqueda híbrida, combinando coincidencias textuales y semánticas. Elegir biblioteca, motor y embeddings al conocer tamaño y requisitos; no fijar stack anticipadamente. Exponer una interfaz de búsqueda acotada mediante herramienta local o integración apropiada a Codex.

Flujo: ingesta → limpieza → fragmentos → metadatos → indexación → filtros → recuperación → referencias → lectura de fuente cuando importe.

Metadatos mínimos: ID estable, proyecto, tipo, ruta o URL fuente, fecha de actualización, estado de vigencia, documento sustituido si existe y hash de contenido. Chunking por secciones con encabezados y contexto suficiente, evitando fragmentos sin sujeto.

Actualizar solo documentos cambiados. Eliminar del índice fuentes borradas; marcar las sustituidas y excluirlas de búsquedas vigentes por defecto. Guardar versión del esquema y del modelo de embeddings para reconstrucción reproducible.

## Presupuesto y evaluación

Presupuesto inicial propuesto: 3 a 5 fragmentos y aproximadamente 2000 tokens por consulta. Ajustar según utilidad y cobertura, sin ocultar truncamiento. Si la respuesta requiere más evidencia, ampliar de forma dirigida.

Comparar contra búsqueda textual: fuentes correctas entre los primeros resultados, relevancia, cobertura de preguntas, filtrado por proyecto, documentos obsoletos, latencia y contexto consumido. Evaluar también el costo de ingesta y mantenimiento, no solo tokens de consulta. Reservar preguntas no usadas para ajustar la búsqueda.

La salida debe incluir fragmento, fuente, fecha, proyecto y condición de vigencia. No devolver textos sin procedencia. El gate de E07 puede concluir que RAG aún no compensa.

## Privacidad y contenido no confiable

No indexar secretos. Mantener exportaciones crudas e índices fuera de Git por defecto. Revisar qué corpus puede cruzar proyectos. Un índice local no implica cómputo local: embeddings externos envían texto y los fragmentos incluidos en una llamada remota salen de la máquina. Documentar estas decisiones antes de la ingesta.

Contenido recuperado puede contener instrucciones maliciosas o desactualizadas: tratarlo como datos y nunca permitir que cambie roles, permisos o comandos por sí solo. Probar esa condición durante la evaluación.

## Aprendizajes

Después de un bug, registrar causa y prevención en un documento pequeño. Promover solo reglas generales a AGENTS.md. Indexar el learning curado y conservar vínculo al caso; no duplicar indiscriminadamente chats completos.
