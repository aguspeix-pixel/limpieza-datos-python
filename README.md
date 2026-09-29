# Limpieza automática de datos de ventas con Python

Script en Python (pandas) que toma un archivo de ventas desordenado y lo deja limpio y listo para analizar.

## Problema que resuelve

Los archivos de ventas suelen llegar con errores que impiden analizarlos:

- Nombres con espacios de más y mayúsculas mezcladas ("ANA PEREZ", " Ana Perez")
- Clientes vacíos
- Montos con coma decimal ("3500,50") que no se pueden sumar
- Fechas en distintos formatos (2026-09-01 y 01/09/2026)
- Filas duplicadas

## Qué hace el script

1. Elimina espacios y unifica mayúsculas en clientes y productos
2. Completa los clientes vacíos con "Sin nombre"
3. Convierte los montos a números
4. Unifica todas las fechas en un solo formato
5. Elimina las filas duplicadas
6. Guarda el resultado en un archivo nuevo y calcula el total de ventas

## Cómo usarlo

1. Instalar las librerías: `py -m pip install pandas`
2. Generar datos de ejemplo: `py generar_datos.py`
3. Limpiar los datos: `py limpiar_datos.py`

El resultado queda en `ventas_limpias.csv`.

## Ejemplo

Antes: 6 filas con errores. Después: 4 filas limpias y consistentes.

## Tecnologías

Python, pandas

## Contacto

¿Necesitás limpiar o automatizar tus datos? Escribime.