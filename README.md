# Asistente de Juli

Esta carpeta le da a un asistente de IA instrucciones para ayudar a Juli con su trabajo de coordinación. Podés empezar con un caso ficticio y usar la estructura como guía para tus primeras tareas.

## Empezar en una computadora

1. Descomprimí el paquete en una carpeta propia. Si ya tenés la carpeta base, podés usarla directamente.
2. Abrila como carpeta de trabajo en Codex o en una herramienta autorizada que admita instrucciones de proyecto. En Codex, usá la carpeta que contiene `AGENTS.md`. Si tu herramienta no carga ese archivo automáticamente, agregá su contenido como instrucciones del proyecto si ofrece esa opción.
3. Probá con este pedido. «Usá el flujo de seguimiento con este caso ficticio. Falta confirmar la fecha de una capacitación y preparar la agenda de la próxima reunión. Armá una lista de pendientes y marcá qué falta confirmar».
4. Revisá que el asistente distinga lo confirmado de lo pendiente. Si querés ajustar el idioma o el nivel de detalle, editá `context/perfil.md`.

Para cada conversación nueva en Codex, seleccioná esta carpeta como proyecto o carpeta de trabajo. La instrucción de inicio está en `AGENTS.md` y le pide al asistente leer tu perfil y preferencias antes de responder. Si el saludo o la respuesta no reflejan ese contexto, comprobá que abriste esta carpeta y pedile que lea `AGENTS.md` y `context/perfil.md`.

El asistente funciona con los archivos de texto incluidos. Si querés anotar preferencias locales, copiá `config/config.example.json` como `config/config.local.json` y pedile al asistente que lo lea. Es un ejemplo opcional que se lee bajo pedido. Las conexiones y el acceso a tu cuenta se configuran en la herramienta que uses.

Mientras trabajás, el asistente puede guardar preferencias y procesos reutilizables que le enseñes, siempre que sean seguros y estén autorizados. Te avisará qué guardó. Podés pedirle que te muestre, corrija o borre esa información. Para volver a usarla en otra computadora, consultá las indicaciones de migración.

Cada estudio y cada trabajo que necesite continuidad tendrá un archivo `progress.md` con su estado, pendientes y próximo paso. El asistente lo actualizará para retomar el trabajo en otra conversación. Podés pedirle que te muestre el estado o que corrija lo que figure allí.

## Dónde va cada cosa

| Ruta | Para qué sirve |
| --- | --- |
| `AGENTS.md` | Instrucciones del asistente y límites de privacidad |
| `config/` | Ejemplo de preferencias locales |
| `context/` | Perfil de trabajo y preferencias generales |
| `knowledge/` | Guía para usar referencias autorizadas |
| `workflows/` | Pasos para tareas frecuentes |
| `tasks/` | Plantillas y carpetas locales de trabajos que no pertenecen a un estudio |
| `memory/` | Guía para conservar preferencias autorizadas |
| `workspace/` | Área local de entrada y salida para material ficticio o no sensible autorizado |
| `skills/` | Espacio para futuras capacidades reutilizables |
| `studies/` | Guía y plantilla para ordenar cada estudio y sus pendientes operativos seguros |

## Migrar a otra computadora

1. Cloná el repositorio privado o prepará una copia del proyecto con las carpetas de estudios, trabajos, procesos y memoria autorizados. Incluí los archivos ocultos `.gitignore` y `.gitkeep`.
2. Revisá el contenido antes de transferirlo. Dejá afuera credenciales, configuraciones locales de conexión y archivos que la institución no autorice para el destino. Configurá las conexiones en la nueva computadora.
3. Abrí la carpeta en la nueva computadora y repetí la prueba ficticia. Iniciá sesión desde la herramienta si hace falta.

Si usás Git, las reglas de exclusión ayudan a mantener archivos locales fuera de los cambios nuevos. Un ZIP hecho a mano puede incluir archivos ignorados, y Git sigue registrando los archivos ya versionados. Revisá el contenido antes de compartirlo. Guardá los datos clínicos y documentos confidenciales en los sistemas institucionales autorizados.
