# coding=utf-8
# lexer
tokens = ('ANNO', 'MES', 'DIA', 'HORA', 'SEPARADOR', 'TIMEZONE', 'ESPACIO', 'FORMATO', 'NUM')


def t_ANNO(t):
    r"""y[12][0-9]{3}"""
    return t


def t_MES(t):
    r"""(((Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|June?|July?|Aug(ust)?|Sep(t(ember)?)?|Oct(ober)?|Nov(ember)?|Dec(ember)?))|m(0[1-9]|1[0-2]))"""
    return t


def t_DIA(t):
    r"""d(0[1-9]|[12]\d|3[01])"""
    return t


def t_ESPACIO(t):
    r"""\s+"""
    return t


def t_HORA(t):
    r"""^(?:\d|[01]\d|2[0-3]):[0-5]\d$"""
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
    """fecha : M C D C A E"""
    # print(p[2], end="")


def p_dia(p):
    """D : DIA"""
    print(p[1], end="")


def p_espacio(p):
    """E : ESPACIO"""
    print(p[1], end="")


def p_separador(p):
    """C : SEPARADOR"""
    print(p[1], end="")


def p_mes(p):
    """M : MES"""
    print(p[1], end="")

def p_anno(p):
    """A : ANNO"""
    print(p[1], end="")


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
