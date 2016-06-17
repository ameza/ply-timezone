# ply-timezone #
timezone converter ply para curso automátas y compiladores

*El lenguaje consistirá en una fecha y hora en varios formatos (serán utilizados los nombres de meses en inglés o sus abreviaciones), una zona horaria de origen y una zona horaria de destino, opcionalmente se puede especificar el formato de salida o añadir días.

*También se podrán obtener diferencias entre fechas completas con diferentes zonas horaria.

Python 3.4.3

###Workspace para probar código###

https://ide.c9.io/ameza1/andres-ply-timezone

###Bibliotecas utilizadas###

*ply*

```pip3 install ply```

*simple-dates*

```pip3 install simple-dates```

###Casos de prueba:###

```19/Nov/1989 13:22 UTC PST ADD 400 mm/dd/yyyy```

```16-12-1991 19:00 UTC 09/19/2016 18:30 PST```

```December 16 1991 19:00 PST UTC```

```16/12/1991 12:00 UTC PST```

```Dec 16 1991 13:00 UTC PST```

```12/16/1991 17:00 UTC PST```

```16-12-1991 19:00 PST CST ADD 30 dd/mm/yyyy```

```December 16 1991 19:00 UTC 12/16/2016 18:00 PST```

```16-12-1991 19:00 UTC 12/16/2016 18:00 PST```
