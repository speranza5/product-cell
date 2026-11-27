# Plantillas de agentes

Estos archivos son propuestas sin activar. En E02 revisar instrucciones del piloto, ajustar modelos disponibles e instalar en `.codex/agents/` del proyecto elegido. No copiar AGENTS.md de este repo sobre el de un tracker sin integrarlo.

Modelos propuestos: PM y Tech Lead con gpt-6.2-sol/medium, Reviewer con gpt-6.2-sol/medium, Dev y DevOps con gpt-6-luna/high. El coordinador es el agente principal, configurado en el cliente; no hay un subagente adicional coordinador.

Las plantillas fijan modelo y esfuerzo. Para escalar una tarea, seleccionar otro agente/configuración efectiva o actualizar el archivo con intención; una preferencia verbal no debe presentarse como cambio comprobado si el archivo sigue fijando otro modelo. Registrar modelo observado cuando el cliente lo permita.

Los permisos y herramientas reales proceden de la sesión y su entorno. No suponer que estos TOML crean aislamiento. Cada asignación debe incluir el contrato de docs/HARNESSES.md. En E02 se instala primero Spec Kit y el enrutamiento mínimo; una skill product-cell se crea solo si aporta reutilización. No está instalada aquí. Cada especialista actúa sobre los artefactos canónicos de Spec Kit y no repite etapas ya completadas.
