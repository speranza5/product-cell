# Arneses y subagentes

Base de ejecución elegida: [Spec Kit](SPEC_KIT.md). Aplicar la [política de tokens](TOKEN_POLICY.md); las instrucciones por rol complementan sus procesos sin volver a ejecutarlos dentro de cada agente.

## Contrato común

Cada asignación incluye tarea, modo, etapa, estado, objetivo, versión de spec, aceptación, fuentes obligatorias, archivos permitidos, herramientas disponibles, límites, verificación y salida. La disponibilidad real de herramientas y modelos se verifica en el entorno.

El arnés combina instrucciones, selección de contexto, herramientas, permisos, estado y validaciones. Un archivo TOML con una personalidad no alcanza. Las instrucciones del rol son acuerdos; permisos del entorno y CI son mecanismos de control distintos.

## Responsabilidades

| Rol | Entrada | Decisiones | Salida | Escalamiento |
|---|---|---|---|---|
| Coordinador | Solicitud y estado | Clasificación y siguiente paso | Estado y handoff | Intención o alcance ambiguos |
| PM | Contexto y evidencia | Propuesta funcional dentro de objetivos | Aceptación y experiencia | Cambio de apuesta de producto |
| Tech Lead | Spec funcional y constraints | Diseño dentro de restricciones | Plan y verificaciones | Cambio de contrato, arquitectura o alcance |
| Dev | Tarea ready | Detalles internos acordes al diseño | Diff y resultados | Decisiones faltantes o fallos repetidos |
| Reviewer | Spec, diff y evidencia | Hallazgos y conformidad | Reproducción y severidad | Evidencia insuficiente o riesgo sin resolver |
| DevOps | Cambio validado y runbook | Ejecución autorizada | Entrega y recuperación | Permisos, incidente o procedimiento ambiguo |

Una revisión independiente cuando corresponda; revisores adicionales requieren riesgos diferentes. No exigir un mínimo de hallazgos. PM y Tech Lead intervienen cuando quedan decisiones pendientes.

Reviewer no debe convertirse en segundo implementador durante la revisión. Si hay hallazgos, devolver al responsable y verificar las correcciones. El coordinador es el único escritor del estado global; agentes editan archivos asignados o devuelven un resumen para integrarlo.

## Economía de contexto

- No instanciar todos los roles. Coordinación, refinamiento y revisión generan costo propio.
- Enviar contexto mínimo suficiente: no omitir reglas obligatorias por ahorrar tokens.
- Reutilizar referencias seleccionadas; evitar búsquedas idénticas por cada rol.
- Preferir una tarea pequeña y verificable antes que una spec enorme.
- Salida usual: resultado, archivos, verificaciones, bloqueos y siguiente acción; máximo orientativo de 300 palabras, ampliable por evidencia necesaria.
- Tras dos intentos equivalentes fallidos, cambiar estrategia o escalar; no confundir límite de intentos con permiso para abandonar sin registrar.
- Paralelizar investigación independiente; evitar editores simultáneos sobre los mismos archivos.
- No repetir pruebas ya aprobadas salvo cambios relevantes, fallos o preocupaciones pendientes.

## Modelos

Propuesta inicial: Sol para coordinación y definición; Luna para implementación cerrada y operación repetible. Refinamiento profundo, migraciones y diagnóstico ambiguo vuelven a modelo fuerte. Reviewer usa modelo fuerte cuando el riesgo lo justifica. Las plantillas fijan defaults de ejemplo; confirmar disponibilidad y configuración efectiva en el piloto.

Medir tokens cuando haya telemetría disponible, tiempo, reintentos y defectos. No prometer un porcentaje de ahorro sin una línea base. Usar la misma clase de tarea para comparar.

## Verificaciones ejecutables

El verificador incluido solo valida estado y enlaces locales. En E02 se podrán incorporar validaciones de campos y pases de tareas. En el piloto, CI verifica comandos reales de lint, tipos, tests, build o migraciones según riesgo. Una salida “aprobado” del agente no reemplaza el resultado de esos comandos.

Permisos y sandbox se heredan de la sesión; las instrucciones de un subagente no crean un entorno aislado. Si hace falta separación estricta de producción, usar entornos y credenciales separados. Las herramientas de despliegue se configuran en el entorno pertinente, no se simulan con prompts.
