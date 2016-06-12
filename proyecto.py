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
    r"""\s+"""
    return t


def t_HORA(t):
    r""":"""
    return t


def t_SEPARADOR(t):
    r"""-|,|\/|\s"""
    return t


def t_TIMEZONE(t):
    r"""^(A|E|C|M|P|AK|H)ST|UTC$"""
    return t


def t_FORMATO(t):
    r"""^(mm\/dd|dd\/mm)\/yyyy$"""
    return t


def t_NUM(t):
    r"""^([1-9][0-9]{0,2}|1000)$"""
    return t


# tokens default
# t_ignore = "\t"


def t_error(t):
    print("¡Error léxico!")
    t.lexer.skip(1)


def t_newline(t):
    r"""\n"""
    t.lexer.lineno += t.value.count("\n")


import ply.lex as lex

lex.lex()


# parser`
def p_oceano_con_olas(p):
    """P : M C D C A E H
         | D C M C A E H"""
 #   print(p.lexer.lexdata, end="")


def p_dia(p):
    """D : DIGITO DIGITO"""
    try:
        total = int(p[1]+p[2])
        if 0 < total < 32:
            p[0] = total
            print(p[0], end="")
        else:
            print("El día debe estar entre 1 y 31")
            p.lexer.skip(1)
    except ValueError:
        print("Invalid integer", total)
        p[0] = 0

def p_espacio(p):
    """E : ESPACIO"""
    print(p[1], end="")


def p_separador(p):
    """C : SEPARADOR"""
    print(p[1], end="")


def p_mes(p):
    """M : DIGITO DIGITO
         | MES"""
    try:
        if p[1].isalpha():
            p[0] = p[1]
            print(p[0], end="")
        else:
            total = int(p[1]+p[2])
            if 0 < total < 13:
                p[0] = total
                print(p[0], end="")
            else:
                print("El mes debe estar entre 1 y 12")
                p.lexer.skip(1)
    except ValueError:
        p[0] = p[0]


def p_anno(p):
    """A : ANNO"""
    print(p[1], end="")


def p_hora(p):
    """H : DIGITO DIGITO HORA DIGITO DIGITO  """
    hora = int(p[1] + p[2])
    if -1 < hora < 24:
        minuto = int(p[4] + p[5])
        if -1 < minuto < 60:
            p[0] = p[1]+p[2]+p[3]+p[4]+p[5]
            print(p[0], end="")
        else:
            print("Los minutos deben estar entre 00 y 59")
        p.lexer.skip(1)
    else:
        print("La hora debe estar entre 00 y 23")
        p.lexer.skip(1)



def p_error(p):
    print("¡Error sintáctico!")


import ply.yacc as yacc

yacc.yacc()

while 1:
    try:
        print("\n")
        oceano = input("oceano>")
    except EOFError:
        break
    if not oceano:
        continue
    yacc.parse(oceano)
