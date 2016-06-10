# coding=utf-8
# lexer
tokens = ('OLA', 'AGUA', 'PEZ')

t_AGUA = r'~'


def t_OLA(t):
    r"""O|o"""
    if t.value == 'o':
        t.value = ',.,~\'`\'~,.,'
    else:
        t.value = '_.,-*~\'`^`\'~*,._'
    return t


def t_PEZ(t):
    r"""P|p"""
    if t.value == 'P':
        t.value = '/><}}}}}*>'
    else:
        t.value = '/><}}}*>'
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
    """oceanos : AGUA objeto AGUA"""
    print(p[3], end="")

def p_objeto(p):
    """objeto : olas test olas"""


def p_ola(p):
    """olas : OLA"""
    print(p[1], end="")

def p_pez(p):
    """peces : PEZ"""
    print(p[1])

def p_test(p):
    """test : peces
    | objeto """




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
