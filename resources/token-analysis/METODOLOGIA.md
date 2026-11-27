# Medición estática de BMAD y Spec Kit

Fecha: 2026-11-27. Se descargaron repositorios públicos en carpetas temporales y se inspeccionaron instrucciones como datos. No se instalaron ni ejecutaron los workflows de los frameworks. No se enviaron tareas de implementación a modelos ni se midió facturación.

## Versiones

- Spec Kit v1.4.5, commit `6ba8beefff8d6408cadd62038e92d459093e33a8`.
- BMAD v6.12.4, commit `bab9082c3e884e0d72c759bcd1a6d90bcc01be84`.
- tiktoken 0.14.0, codificación `o200k_base`.

Estos eran los tags devueltos por releases/latest de GitHub al consultar. La documentación web de BMAD describe defaults más recientes; no se mezclaron con los defaults del tag para los hallazgos del código.

## Qué significan los números

Los conteos son exactos para el texto fuente y la codificación elegida. No son tokens de ejecución de Codex ni garantizan equivalencia con el tokenizador de cada modelo. Se incluyen Markdown, comentarios y placeholders presentes en el archivo. La instalación/renderización puede transformar ese texto.

Cada grupo suma archivos fuente una sola vez. No simula cuántas veces se envían en peticiones posteriores. No cuenta prompts de sistema, herramientas, instrucciones del proyecto, documentos generados, código, diff, logs, razonamiento, revisiones repetidas ni caché.

Los grupos no representan trabajos funcionalmente equivalentes: Spec Kit SDD incluye definición de requisitos; BMAD build no representa su discovery completo. BMAD parent excluye las instrucciones inyectadas desde customize.toml, archivos condicionales y subagentes. Las instrucciones de dos revisores se enumeran aparte. No usar sus cocientes como porcentaje de ahorro.

## Archivos de evidencia

- `source-counts.csv`: conteo por archivo.
- `groups.json`: agrupaciones y miembros exactos.
- `measure.py`: script reproducible, con tiktoken instalado en el entorno elegido.

Ejemplo de reproducción:

```sh
python measure.py /ruta/spec-kit /ruta/bmad /ruta/resultados
```

Antes de reproducir, hacer checkout de los commits indicados. La tabla del tokenizador requiere descarga inicial; los textos se tokenizan localmente.

## Hallazgos verificables en los tags

Spec Kit: la integración Codex instala skills. implement.md requiere tasks.md y plan.md y enumera otras fuentes si existen. Los comandos analyze y converge indican carga progresiva. La extensión bug separa assessment, fix y test, con reportes y hooks. Eso aporta trazabilidad, pero agrega texto y pases para bugs pequeños.

BMAD: bmad-build carga pasos a demanda, propone specs de 900 a 1600 tokens y define una ruta oneshot. La ruta completa configura tres capas de revisión, la oneshot una. step-04-review exige revisores de la misma capacidad que la sesión. El revisor blind-hunter pide un mínimo de hallazgos; esta política puede inducir investigación y triage adicionales, sin que esta inspección demuestre falsos positivos reales. Ciertos hallazgos disparan reversión y reimplementación, con límite de iteraciones.

## Conclusión limitada

La inspección no demuestra que Spec Kit consuma menos. Identifica dos mecanismos de costo diferentes: documentación/comandos y relecturas en Spec Kit; fan-out de revisión y loopbacks en BMAD. El resultado depende del modo, riesgo, versión, personalización y retrabajo evitado.

## Piloto propuesto

Primera ronda: cuatro casos idénticos por framework (brief fundacional con evidencia fija, historia, tweak, bug con reproducción), mismo commit inicial y mismos criterios de aceptación. Ocho ejecuciones, sin paralelizar escritoras sobre la misma copia. Fijar versión, modelo/esfuerzo por rol, corpus, política de revisión y estado de caché observable. Alternar orden de frameworks. No confundir ese primer sondeo con evidencia estadística.

Registrar todas las llamadas del coordinador y subagentes: entrada total, entrada cacheada como subconjunto cuando la telemetría así lo define, salida, razonamiento según la definición del proveedor, invocaciones, herramientas, reintentos, contexto máximo, duración, aceptación y defectos. Si falta telemetría, marcar desconocido. Repetir solo los casos que cambien la decisión o tengan variación importante.

Comparar configuración por defecto y ajustada por separado. El indicador principal es costo o consumo agregado hasta aceptación, con la misma calidad exigida. Menor número de tokens con una solución incorrecta no cuenta como ahorro.
