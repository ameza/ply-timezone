# -*- coding: utf-8 -*-
import ply.lex as lex
import datetime
import ply.yacc as yacc
import simpledate
from dateutil.relativedelta import relativedelta

# coding=utf-8
# lexer
tokens = ('ANNO', 'DIGITO', 'MES', 'HORA', 'SEPARADOR', 'TIMEZONE', 'ESPACIO', 'FORMATO', 'NUM')


def t_ANNO(t):
    r"""[12][0-9]{3}"""
    return t


def t_MES(t):
    r"""((Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|June?|July?|Aug(ust)?|Sep(t(ember)?)?|Oct(ober)?|Nov(ember)?|Dec(ember)?))"""
    return t


def t_DIGITO(t):
    r"""[0-9]"""
    return t


def t_ESPACIO(t):
    r"""\s"""
    return t


def t_HORA(t):
    r""":"""
    return t


def t_SEPARADOR(t):
    r"""-|,|\/"""
    return t


def t_TIMEZONE(t):
    r"""(E|C|M|P|H)ST|UTC"""
    return t


def t_FORMATO(t):
    r"""(mm\/dd|dd\/mm)\/yyyy"""
    return t


def t_NUM(t):
    r"""ADD\s([1-9][0-9]{0,2}|1000)"""
    return t


# tokens default
# t_ignore = "\t"


def t_error(t):
    print("\n!Error léxico!\n")
    t.lexer.skip(1)


def t_newline(t):
    r"""\n"""
    t.lexer.lineno += t.value.count("\n")


lex.lex()


# parser`

def p_fecha_conversion(p):
    """S : P X X F K
         | P X X K F
         | P X X
         | P X X F
         | P X X K
         | P X E P X"""

    # si el tercer no terminal esta vacío significa que se están comparando fechas
    if p[3] == " ":
        print('\nCalculando tiempo transcurrido entre fechas ingresadas')

        nuevoP2 = simpledate.best_guess_utc('{} {}'.format(p[1], p[2]), debug=False)

        nuevoP5 = simpledate.best_guess_utc('{} {}'.format(p[4], p[5]), debug=False)

        delta = relativedelta(nuevoP5, nuevoP2)
        print("\nTotal: \n{} Años \n{}  Meses \n{} Días\n{} Horas \n{} Minutos".format(delta.years, delta.months,
                                                                                       delta.days, delta.hours,
                                                                                       delta.minutes))
    else:
        print("\nConvirtiendo de {} a {}".format(p[2], p[3]), end='')
        formatoSalida = '%B/%d/%Y %H:%M'
        anadirTotal = 0
        # en este punto verificamos si es requerido añadir días o proveer un formato de salida
        if len(p) > 4:
            if p[4] is not None:
                if p[4].isdigit():
                    print("\nSe añadirán {} días a resultado".format(p[4]), end='')
                    anadirTotal = p[4]
                else:
                    print("\nFormato de salida: {}".format(p[4]), end='')
                    if p[4] == ' mm/dd/yyyy':
                        formatoSalida = '%m/%d/%Y %H:%M'
                    else:
                        formatoSalida = '%d/%m/%Y %H:%M'
        if len(p) > 5:
            if p[5] is not None:
                if p[5].isdigit():
                    print("\nSe añadirán {} días a resultado".format(p[5]), end='')
                    anadirTotal = p[5]
                else:
                    print("\nFormato de salida: {}".format(p[5]), end='')
                    if p[5] == ' mm/dd/yyyy':
                        formatoSalida = '%m/%d/%Y %H:%M'
                    else:
                        formatoSalida = '%d/%m/%Y %H:%M'

        fechaFinal = p[1] + datetime.timedelta(days=int(anadirTotal))

        dateConversion = simpledate.SimpleDate('{} {}'.format(fechaFinal, p[2]), unsafe=True, debug=False) \
            .convert(tz='{}'.format(p[3]), unsafe=True)
        print('\nResultado:', dateConversion.datetime.strftime(formatoSalida), p[3])

        print('\nDST No se encuentra activo en esta conversión')


def p_fecha_hora(p):
    """P : M C D C A E H
         | M E D E A E H
         | D C D C A E H
         | D E D E A E H
         | D E M E A E H
         | D C M C A E H"""
    try:
        # revisamos los no terminales para idenficar el formato de tiempo recibido
        if p[1].isalpha():
            if len(p[1]) > 3:
                formato = "%B" + p[2] + "%d" + p[4] + "%Y %H:%M"
            else:
                formato = "%b" + p[2] + "%d" + p[4] + "%Y %H:%M"
        elif p[3].isalpha():
            if len(p[3]) > 3:
                formato = "%d" + p[2] + "%B" + p[4] + "%Y %H:%M"
            else:
                formato = "%d" + p[2] + "%b" + p[4] + "%Y %H:%M"
        elif 0 < int(p[1]) < 13:
            formato = "%m" + p[2] + "%d" + p[4] + "%Y %H:%M"
        elif 0 < int(p[1]) < 13:
            formato = "%d" + p[2] + "%m" + p[4] + "%Y %H:%M"
        else:
            formato = "%d" + p[2] + "%m" + p[4] + "%Y %H:%M"

        # hora por defecto en caso de que el parsing de la hora fuera inválido
        if p[7] is None:
            hora = "00:00"
        else:
            hora = p[7]
        mifecha = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + hora
        fecha = datetime.datetime.strptime(mifecha, formato)
        print("\nFormato reconocido: {}\nFecha Reconocida: {}".format(formato, fecha), end='')
        p[0] = fecha
    except ValueError:
        # raise
        print("\nLa fecha ingresada es inválida\n")
        p[0] = 0
        p.lexer.skip(1)


def p_espacio_timezone(p):
    """X : E T"""
    p[0] = p[2]


def p_doble_digito(p):
    """D : DIGITO DIGITO"""
    p[0] = p[1] + p[2]
    # print(p[0], end="")


def p_espacio(p):
    """E : ESPACIO"""
    p[0] = p[1]
    # print(p[1], end="")


def p_formato(p):
    """F : E FORMATO"""

    if len(p) > 1:
        p[0] = p[1] + p[2]


def p_anadir_dias(p):
    """K : E NUM"""

    if len(p) > 1:
        p[0] = p[2][4:]


def p_separador(p):
    """C : SEPARADOR"""
    p[0] = p[1]
    # print(p[1], end="")


def p_mes(p):
    """M : MES"""
    p[0] = p[1]
    # print(p[0], end="")


def p_anno(p):
    """A : ANNO"""
    p[0] = p[1]
    # print(p[1], end="")


def p_hora(p):
    """H : DIGITO DIGITO HORA DIGITO DIGITO"""
    hora = int(p[1] + p[2])
    if -1 < hora < 24:
        minuto = int(p[4] + p[5])
        if -1 < minuto < 60:
            p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
            # print(p[0], end="")
        else:
            # raise ValueError("Los minutos deben estar entre 00 y 59")
            print("Los minutos deben estar entre 00 y 59")
            p.lexer.skip(1)
    else:
        # raise ValueError("La hora debe estar entre 00 y 23")
        print("La hora debe estar entre 00 y 23")
        p.lexer.skip(1)


def p_timezone(p):
    """T : TIMEZONE"""
    p[0] = p[1]


def p_error(p):
    print("\n¡Error sintáctico! \n")


yacc.yacc()

while 1:
    try:
        print("\n")
        tzparser = input("tzparser_andres>")
    except EOFError:
        break
    if not tzparser:
        continue
    yacc.parse(tzparser)
