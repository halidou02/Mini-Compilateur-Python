import ply.lex as lex
import sys

reserved_words={
    'tantque':'TANTQUE',
    'entier' : 'ENTIER',
    'main':'Main',
    'ecrire':'ECRIRE',
    'si':'SI',
    'sinon':'SINON',
    'lire':'LIRE',
    'alors':'ALORS',
    'faire':'FAIRE',
    'retour':'RETOUR',
}

tokens = (
    'NUMBER',
    'ADD_OP',
    'MUL_OP',
    'LPAREN',
    'RPAREN',
    'ENDLINE',
    'ID',
    'AFFECT',
    'LOGC_OP',
    'LSEPARATEUR', 
    'RSEPARATEUR',
    'LCROCHET',
    'RCROCHET',
    'STRING',
    'COMMA'
)+tuple(map(lambda s:s.upper(),reserved_words))

t_ADD_OP = r'\+|\-'
t_MUL_OP = r'\*|\/'
t_LOGC_OP=r'\&|\||\!|\!\=|\=\=|\>\=|\<\=|\>|\<'
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_ENDLINE=r'\;'
t_AFFECT =r'\='
t_LSEPARATEUR=r'\{'
t_RSEPARATEUR=r'\}'
t_LCROCHET = r'\['
t_RCROCHET =r'\]'
t_STRING = r'\'(.*)\''
t_COMMA  = r'\,'
#t_COMMENTS = r'\#.*'
t_ignore = ' \t \n'
t_ignore_comments = '\#.*'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_-]*'
    if t.value in reserved_words:
        t.type= t.value.upper()
    return t

def t_NUMBER(t):
    r'\d+(?![a-zA-Z_])'         #les alphabet et _ n'exsist jamais aprés le numero
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Not Accepted")
    exit(1)

lexer = lex.lex()

def read_file(filename):
    with open(filename, 'r') as file:
        f = (file.read())
    return f    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: missing file argument")
        sys.exit(1)
    filename = sys.argv[1]
    prog =read_file(filename)
    lexer = lex.lex()
    lex.input( prog )
    while True:
        tok = lexer.token()
        if not tok:
            break # No more input
    print("Accepted")