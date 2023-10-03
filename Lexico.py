import ply.lex as lex

tokens = (
    'NUMERO',
    'OPEREL',
    'PC',
    'ID',
    'SIGNO'
)

t_OPEREL = r'[<=]'
t_SIGNO = r','

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PC(t):
    r'[Ss][Ee][Ll][Ee][Cc][Tt]|[Ff][Rr][Oo][Mm]|[Ww][Hh][Ee][Rr][Ee]'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"No es aceptado :( -> '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

data = 'SELECT col1, col2 from mi_Tabla wHERE col1 < 20'
lexer.input(data)

for token in lexer:
    print(f"{token.type}: {token.value}")
