# Estado actual

Actualizado: 2026-11-28, America/Argentina/Buenos_Aires.

## Último paso completado

**E00 — Base documental.** Se creó un repositorio Git independiente con README, guía paso a paso, cuatro recorridos, contratos de arneses, plan gradual de RAG, plantillas y registro persistente de avance.

## Última adaptación completada

Spec Kit elegido como base del piloto. Incorporados el análisis reproducible de tokens, fuentes canónicas, política de consumo y guía de instalación versionada. Esto no completa E01 ni E02.

## Dónde estamos

- Etapa de construcción: E01, pendiente de inicio.
- Etapa del producto piloto: aún no definida.
- Modo del trabajo actual: fundacional.
- Tarea activa: ninguna.
- Próximo responsable: coordinador con el usuario.
- Próxima acción: identificar el repo piloto y reunir sus instrucciones y decisiones existentes.

## Información necesaria para E01

- Elegir Gym Tracker o CEDEAR Tracker e indicar su ruta local o repo accesible.
- Identificar los materiales relevantes de Claude o ChatGPT que se incorporarán.
- Confirmar si las cinco customer questions propuestas coinciden con el método usado.

Estas elecciones no bloquean la base documental entregada; son entradas del próximo paso.

## Capacidades reales

| Componente | Estado |
|---|---|
| Repositorio y documentación | Creado |
| Estado persistente y verificador | Creado y verificado |
| Contexto de trackers | Pendiente de incorporar |
| Spec Kit | Elegido; guía v1.4.5 lista; no instalado en un piloto |
| Recurso de tokens | Conteos estáticos importados; no benchmark de ejecución |
| Agentes personalizados | Plantillas, aún no instaladas |
| Skill product-cell | Enrutamiento mínimo si el piloto lo necesita; sin duplicar workflows de Spec Kit |
| Pruebas de flujo con agentes | Pendientes |
| CI y despliegue | Pendientes de adaptar al piloto |
| Búsqueda documental y RAG | Planificados, no implementados |
| Remoto Git | GitHub privado: https://github.com/speranza5/product-cell |

## Evidencia y continuación

La verificación inicial se registra en docs/LOG.md. Ejecutar `python3 scripts/check_state.py` y consultar Git para comprobar la revisión actual. No usar este documento como prueba de capacidades futuras.

Prompt:

> Retomá E01 según docs/SETUP.md. Primero verificá el estado y localizá los materiales del piloto que te indique. Consolidá contexto y constraints con fuentes. No instales Spec Kit ni agentes hasta completar esta etapa. Después seguí docs/INSTALL_SPEC_KIT.md para E02.
