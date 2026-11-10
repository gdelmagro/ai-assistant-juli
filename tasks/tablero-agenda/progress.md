# Tablero de agenda de Juli

- Última actualización: 2026-11-10.
- Fuente: pedido de Ger y explicación de Juli en esta conversación.
- Objetivo: tablero de lectura de la agenda de diabetes, con actualización al abrir y descarga Excel de datos filtrados de GZBZ, Redefine y Elimunate 2.
- Avances: Ger autorizó el uso de la agenda real en modo de solo lectura. Revisados encabezados de la hoja modelo y una semana real. Se preparó una primera versión local en `app/`, con OAuth de Google, filtros de semana y estudio y exportación XLSX sin nombres. Se comprobó la interfaz inicial y la generación de XLSX con una fila ficticia.
- Pendientes: validar la interpretación de filas reales, variantes de protocolo, distribución por días y duplicados con Juli. Según Juli, el amarillo indica habitualmente visita realizada y el tachado indica ausencia. Se aplican a la fila salvo la celda Protocolo, que suele conservar el color del estudio, por ejemplo verde para Redefine. Una fila tachada también puede estar oculta. El tablero actual no interpreta esas señales visuales ni distingue filas ocultas.
- Configuración: proyecto Google Cloud y OAuth configurados por Ger. Se quitó la configuración de conexión de la interfaz por pedido de Ger. El 2026-11-10 se comprobó que al abrir el tablero obtuvo automáticamente la lista de pestañas con la sesión de Google activa. La sesión puede requerir autorización posterior de Google.
- Selector: se selecciona la semana actual y las opciones se ordenan de fecha más reciente a más antigua. Ger indicó priorizar el formato estandarizado, interpretado como la pestaña cuyo título contiene solo el rango de fechas. Si hay otra ambigüedad o no existe semana actual, queda pendiente la elección. Verificado con datos de prueba el 2026-11-10. La referencia posterior de Ger a «semana más reciente» queda por confirmar frente a su preferencia anterior de semana actual.
- Vista: el 2026-11-10 Ger señaló información faltante. Se agregó la columna de médica, que ya se leía para el Excel. La versión excluye nombres de pacientes y la columna Otros. Pendiente validar la lectura con Juli y confirmar qué datos adicionales necesita.
- Agenda 2027: Ger indicó que por ahora no quiere incorporarla. El tablero conserva la agenda 2026.
- Bloqueos: falta validar la lectura de filas y los campos omitidos. La descarga incluye códigos y debe usarse según los procedimientos institucionales.
- Próximo paso: probar la semana actual con la pestaña de formato estandarizado y validar la información junto a Juli.
- Archivos relacionados: `workflows/agenda-diabetes.local.md` y fichas de los tres estudios en `studies/`.
