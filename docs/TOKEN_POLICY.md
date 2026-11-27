# Política de consumo y evidencia

## Resultado que buscamos

Minimizar consumo hasta una tarea aceptada, con verificación adecuada al riesgo. Menos tokens con un resultado incorrecto no es ahorro. La elección de Spec Kit se basa en adaptabilidad, no en un ahorro probado frente a BMAD.

## Evidencia disponible

La inspección estática del 27 de noviembre de 2026 midió 37 archivos con tiktoken 0.14.0 y o200k_base. [Metodología y reproducción](../resources/token-analysis/METODOLOGIA.md), [CSV](../resources/token-analysis/source-counts.csv), [grupos](../resources/token-analysis/groups.json).

| Conjunto de archivos fuente | Tokens |
|---|---:|
| Spec Kit v1.4.5 specify, plan, tasks, implement, converge | 15190 |
| Spec Kit clarify y analyze adicionales | 7343 |
| Spec Kit bug assess, fix, test | 8224 |
| Spec Kit cinco comandos de assessment | 9271 |
| BMAD v6.12.4 archivos principales de build completo | 9877 |
| BMAD archivos principales de oneshot | 7774 |
| BMAD dos instrucciones adicionales de revisores | 3875 |

No son recorridos equivalentes ni una factura. Cada fuente se cuenta una sola vez; faltan renderización, instrucciones inyectadas, sistema, herramientas, código, artefactos, salidas, razonamiento y repeticiones. No concluir un porcentaje de ahorro entre filas. El tokenizer de un modelo puede diferir.

## Reglas operativas

- Seleccionar modo antes del procedimiento. Tweak no activa SDD por defecto.
- PM/Tech Lead intervienen por decisiones pendientes, no por ceremonia.
- Una revisión independiente por defecto cuando el cambio la requiera; más revisores solo para riesgos distintos y justificados.
- No exigir un mínimo de hallazgos. Sin hallazgos es un resultado válido.
- Cada hecho y estado tiene una fuente canónica. Handoffs enlazan; no duplican spec, tareas o logs.
- Modelo económico para ejecución delimitada; modelo fuerte para ambigüedad, diagnóstico difícil o alto riesgo. Evaluar retrabajo y no solo el primer intento.
- Agrupar tareas cohesionadas. No crear un agente por microtarea automáticamente.
- No leer todo en el coordinador antes de asignarlo al especialista. Sí asegurar que cada agente recibe las restricciones obligatorias.
- Leer salida resumida de comandos; ampliar logs cuando sea necesario para el diagnóstico.
- No repetir pruebas exitosas sin cambio relevante o duda concreta; respetar gates obligatorios del repo/proceso.
- Tras dos intentos equivalentes fallidos, cambiar diagnóstico o escalar con evidencia.
- RAG responde preguntas concretas; no adjuntar antecedentes por defecto.
- No reducir contexto o desactivar gates a escondidas para alcanzar un número.

## Presupuestos iniciales orientativos

Estado de enrutamiento breve, idealmente hasta 500 tokens; handoff hasta 300 palabras; recuperación histórica inicial de 3 a 5 fragmentos y unos 2000 tokens. Estos son objetivos blandos, nunca razones para omitir una restricción, evidencia o aceptación. No se ha fijado un presupuesto total de ejecución ni un límite económico: se calibrarán con el piloto.

## Cómo medir

Usar [RUN_METRICS.csv](../templates/RUN_METRICS.csv) para resultados por ejecución y [CALL_METRICS.csv](../templates/CALL_METRICS.csv) para llamadas cuando exista telemetría. Registrar coordinador y todos los subagentes con run_id común. Valores desconocidos vacíos; nunca ceros inventados. templates/METRICS.csv se conserva como plantilla histórica; las nuevas mediciones usan RUN_METRICS y CALL_METRICS.

Separar entrada total, parte cacheada y salida. Si el proveedor incluye razonamiento dentro de salida, no volver a sumarlo. Registrar las definiciones de la telemetría y proveedor en el informe de la ejecución. No convertir cuota de suscripción de Codex a dólares usando precios API sin equivalencia demostrada.

Costo API, solo con tarifas y contabilidad conocidas: suma por llamada y modelo de entrada no cacheada por su tarifa, entrada cacheada por la suya y salida facturable por la suya. Si cached input es subconjunto de input total, restarlo antes de calcular la porción no cacheada.

Contexto máximo, consumo agregado, costo y latencia son métricas distintas. Paralelismo puede mejorar latencia y elevar consumo. Una revisión extra debe evaluarse por defectos/retrabajo evitados.

## Piloto elegido

La decisión actual prioriza Spec Kit. E03/E04 calibran sus rutas con tareas reales, sin ejecutar una comparación BMAD completa de forma automática. Si la elección queda en duda, el protocolo comparativo documentado en el recurso usa los mismos cuatro casos por framework, versiones fijas, modelos/esfuerzo y criterios de aceptación comparables. Defaults y configuración ajustada se reportan por separado.

No recomendar porcentajes de ahorro hasta contar con ejecuciones comparables. Repetir solo cuando variación o resultados ambiguos puedan cambiar una decisión.
