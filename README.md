# ply-timezone #
timezone converter ply para curso automátas y compiladores

- El lenguaje consistirá en una fecha y hora en varios formatos (serán utilizados los nombres de meses en inglés o sus abreviaciones), una zona horaria de origen y una zona horaria de destino, opcionalmente se puede especificar el formato de salida o añadir días.

- También se podrán obtener diferencias entre fechas completas con diferentes zonas horaria.

Python 3.4.3

###Workspace para probar código###

Entorno virtual que permite ejecutar y ver el código en el navegador, es necesario crearse una cuenta para poder acceder, el workspace es público.

https://ide.c9.io/ameza1/andres-ply-timezone

###Bibliotecas utilizadas###

*ply*

```pip3 install ply```

*simple-dates*

```pip3 install simple-dates```

###Casos de prueba:###

Convertir una fecha completa a otra zona horaria

December 16 1991 14:35 CST MST

Convertir una fecha completa a otra zona horaria y especificar formato de salida 

Dec/16/1991 14:35 CST EST mm/dd/yyyy

Convertir una fecha completa a otra zona horaria y sumar n días

Dec-16-1991 14:35 HST PST ADD 30 

Convertir una fecha completa a otra zona horaria sumar n días y especificar formato de salida 

16 December 1991 14:35 CST PST ADD 30 mm/dd/yyyy

Dec,16,1991 14:35 CST UTC ADD 20 dd/mm/yyyy

Obtener el tiempo transcurrido entre dos fechas completas

16,12-1991 19:00 UTC 12,16,2016 18:00 PST
