import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS']

t_ignore = ' \t'
t_PLUS   = r'SUM'
t_MINUS  = r'RES'
t_TIMES  = r'MUL'
t_DIVIDE = r'DIV'
t_EQUALS = r'='
t_NAME = r'[a-z]'

def t_NEWLINE(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Tratamiento de errores
def t_error(t):
    print(t.value[0] + " -> Illegal character" )
    t.lexer.skip(1)
	

if __name__ == "__main__":
	f = open ('expresiones.in','r')
	pf = f.read()
	f.close()
	lex.lex()
	lex.input(pf)
	while True:
		tok = lex.token()
		if not tok: break
		print (str(tok.value) + " -> " + str(tok.type))