# Bitácora

Agregar entradas cronológicas con fecha local, alcance, evidencia y próxima acción. No reemplazar el historial con el último resumen.

## 2026-11-27 Base inicial

- Pedido: documentar y construir gradualmente una célula de producto con subagentes, arneses y RAG local; incluir README con estructura y decisiones.
- Completado: E00, repositorio independiente y documentación inicial, plantillas no instaladas y mecanismo de continuidad.
- Verificaciones: registradas al finalizar la creación en la entrada de cierre siguiente.
- Pendientes: E01 a E08. No se modificaron los trackers ni se configuró un remoto.
- Próxima acción: elegir repo piloto, incorporar fuentes y consolidar contexto.

## 2026-11-27 Cierre y verificación de E00

- `python3 scripts/check_state.py`: aprobado; estado, checkboxes del roadmap y enlaces de 15 documentos Markdown coherentes.
- El Python disponible no incluye tomllib; el parseo TOML quedó sin ejecutar. Las cinco plantillas deben validarse con el cliente en E02 antes de instalarlas.
- Verificación negativa del validador: aprobada; una copia temporal con estado incoherente fue rechazada correctamente.
- `git diff --cached --check`: comprobación de whitespace sobre los archivos preparados para el commit inicial.
- E00 completa; E01 todavía no iniciada. Próxima acción: identificar repo piloto y materiales fuente.

## 2026-11-27 Publicación en GitHub

- Publicado por pedido del usuario en https://github.com/speranza5/product-cell.
- Visibilidad privada; origin configurado y rama main subida.
- Actualizados README, estado y registro de decisiones con el destino real.
- El roadmap no cambia: E00 completa; próxima etapa E01.

## 2026-11-27 Adaptación a Spec Kit

- Decisión del usuario: usar Spec Kit con configuración selectiva y política de consumo hasta aceptación.
- Incorporados docs/SPEC_KIT.md, INSTALL_SPEC_KIT.md y TOKEN_POLICY.md; evidencia estática reproducible en resources/token-analysis.
- Actualizados README, continuidad, roadmap, roles y fuentes canónicas para evitar duplicación. D06 sustituida por D12 y D13.
- Agregados fragmento AGENTS para piloto, registro de instalación y métricas por ejecución/llamada.
- Último paso: adaptación documental y de plantillas. E01 sigue pendiente; Spec Kit no está instalado en trackers.
- Próximo paso: elegir piloto, completar E01 y seguir guía E02.
- Verificación de adaptación: enlaces y estado aprobados por scripts/check_state.py; conteos reproducidos contra los dos tags; sintaxis de instalación contrastada con documentación y código de v1.4.5. Instalación real pendiente del piloto.

## 2026-11-28 Continuación de la publicación

- Retomado el commit local de adaptación a Spec Kit. El push anterior no se ejecutó por un fallo de revisión automática asociado al límite de uso.
- Normalizados los finales de línea del CSV y del generador, sin cambiar los conteos.
- Estado y enlaces verificados; E01 sigue pendiente de elección del piloto.
- Se reintenta publicar la adaptación y esta corrección; la confirmación de sincronización se comprueba en Git.
