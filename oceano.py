# coding=utf-8
# lexer
tokens = ('OLA', 'AGUA', 'PEZ')



def t_OLA(t):
    r"""_"""

    return t


def t_AGUA(t):
    r"""((0[1-9]|[1-9]$)|[1-2][0-9]|3[0-1])"""

    return t


# tokens default
t_ignore = " \t"


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
    """oceanos : agua olas"""
    print(p[2])


def p_olas(p):
    """olas : OLA olas"""
    print(p[1], end="")


def p_ola(p):
    """olas : OLA"""
    print(p[1], end="")


def p_peces(p):
    """peces : PEZ peces"""
    print(" " + p[1] + " ", end="")


def p_pez(p):
    """peces : PEZ"""
    print(" " + p[1] + " ", end="")

def p_agua(p):
    """agua : AGUA"""
    print(" " + p[1] + " ", end="")


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
