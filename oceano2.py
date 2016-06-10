# coding=utf-8
# lexer
tokens = ('NUM', 'RESTA', 'SUMA')

t_SUMA = r"""\+"""
t_RESTA = r"""\-"""


def t_NUM(t):
    r"""\d+"""
    try:
        t.value= int(t.value)
    except ValueError:
        print("problem parseando int", t.value)
        t.value = 0
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

def p_resultado(p):
    """resultado : expresion"""
    print(p[1])

def p_expresion(p):
    """expresion : expresion SUMA expresion
                | expresion RESTA expresion """
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_numero(p):
    """expresion : NUM"""
    p[0] = p[1]


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
