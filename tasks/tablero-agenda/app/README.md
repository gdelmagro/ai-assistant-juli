# Tablero de agenda — versión inicial

Se ejecuta en esta computadora y consulta Google Sheets con permiso de lectura. La planilla original no se modifica.

## Preparar Google

1. En Google Cloud, habilitar Google Sheets API en un proyecto autorizado.
2. Configurar el consentimiento OAuth y, si corresponde, agregar la cuenta autorizada como usuaria de prueba.
3. Crear un ID de cliente OAuth de tipo aplicación web y agregar `http://localhost:8765` a los orígenes JavaScript autorizados. No pegar el secreto del cliente.
4. Confirmar que la cuenta de Google elegida tenga acceso a la agenda.

## Iniciar

Desde la carpeta de este proyecto ejecutar:

```sh
python3 server.py
```

Abrir `http://localhost:8765`. El ID de cliente está configurado. El tablero intenta obtener autorización automáticamente al abrirse. Si Google requiere interacción, usar **Actualizar** y completar la autorización solicitada. La aplicación requiere Python con `openpyxl` instalado y conexión a internet. Google solicitará acceso de lectura a las planillas accesibles a la cuenta, según el alcance de Google Sheets. El token de lectura se guarda en el almacenamiento de sesión de la pestaña y se elimina cuando vence o se cierra la pestaña.

Al conectar, ordena las semanas de más reciente a más antigua y consulta la semana actual. Si hay varias pestañas para esa semana, prioriza la única cuyo título contiene solo el rango de fechas. Si aún hay ambigüedad o no hay una pestaña para la semana actual, hay que elegir una. Usar Actualizar para volver a leer los datos. Al recargar la pestaña se reutiliza el token mientras siga vigente. Al cerrar la pestaña o vencer el acceso, el tablero intenta renovar el acceso mediante Google; Google o el navegador pueden requerir interacción.

La vista y la descarga incluyen exclusivamente filas cuyo protocolo coincida con GZBZ, Redefine o Elimunate 2. No incluyen la columna de nombre del paciente ni la columna Otros. La descarga incluye números de participantes, por lo que debe guardarse y usarse según los procedimientos de la institución.

## Estado de validación

Es una primera implementación. La extracción se basa en los encabezados revisados y debe validarse con una cuenta autorizada y con Juli antes de utilizarla para gestionar visitas. En particular, hay que confirmar los nombres con que se escriben los protocolos, la disposición de cada día, las marcas de actividades y la pestaña correcta cuando hay duplicados. Una coincidencia parcial de nombre puede incluir variantes de un protocolo. Se verificó la conexión OAuth y la lectura de los nombres de las pestañas. La lectura de filas reales desde el tablero aún no se validó.
