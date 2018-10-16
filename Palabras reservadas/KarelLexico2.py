import ply.lex as lex

palabrasReservadas = {
	'si' : 'SI',
	'no' : 'NO',
	'apagate' : 'APAGAR',
	'avanza':'AVANZAR',
	'coge-zumbador':'COGER',
	'deja-zumbador':'DEJAR',
	'inicio':'INICIAR',
	'y':'Y',
	'o':'O',
	'entonces' : 'ENTONCES',
	'sino' : 'SINO',
	'mientras' : 'MIENTRAS',
	'hacer' : 'HACER',
	'repetir' : 'ITERACION',
	'veces' : 'VECES',
	'fin' : 'FIN',
	'frente-libre' : 'FRENTELIBRE',
	'frente-bloqueado' : 'FRENTEBLOQUEADO',
	'izquierda-libre' : 'IZQUIERDALIBRE',
	'izquierda-bloqueada': 'IZQUIERDABLOQUEADA',
	'derecha-libre' : 'DERECHALIBRE',
	'derecha-bloqueada' : 'DERECHABLOQUEADA',
	'junto-a-zumbador' : 'JUNTOAZUMBADOR',
	'no-junto-a-zumbador':'NOJUNTOAZUMBADOR',
	'algun-zumbador-en-la-mochila' : 'ALGUNZUMBADORENLAMOCHILA',
	'ningun-zumbador-en-la-mochila' : 'NINGUNZUMBADORENLAMOCHILA',
	'orientado-al-norte' : 'ORIENTADOALNORTE',
	'orientado-al-sur' :	'ORIENTADOALSUR',
	'orientado-al-este' : 'ORIENTADOALESTE',
	'orientado-al-oeste' : 'ORIENTADOALOESTE',
	'no-orientado-al-norte' : 'NOORIENTADOALNORTE',
	'no-orientado-al-sur' : 'NOORIENTADOALSUR',
	'no-orientado-al-este' : 'NOORIENTADOALESTE',
	'no-orientado-al-oeste' : 'NOORIENTADOALOESTE'
}


tokens = ['ID','INS_COMPLETA','GUION','NUMERO','ERROR','DECLARACION','DECLARACIONFINAL','GIRAR','FINALIZAR']



tokens = tokens + list(palabrasReservadas.values())

t_ignore = ' \t'
t_INS_COMPLETA = '\;'
t_GUION = '\-'
t_ignore_COMMENT = r'\{.*'

def t_INICIAR(t):
    r'iniciar-programa'
    return t
	
def t_FINALIZAR(t):
    r'finalizar-programa'
    return t
	
def t_DECLARACION(t):
    r'inicia-ejecucion'
    return t
	
def t_DECLARACIONFINAL(t):
    r'termina-ejecucion'
    return t
	
def t_GIRAR(t):
    r'gira-izquierda'
    return t
	
def t_ERROR(t):
    r'[-a-zA-Z][-a-zA-Z]*'
    t.type = palabrasReservadas.get(t.value,'ERROR')
    return t

	
def t_SALTOLINEA(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
	
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("ERROR -> %s" % t.value)
    t.lexer.skip(1)

if __name__ == "__main__":
	lex.lex()
	f = open ('codigoKarel.in','r')
	pf = f.read()
	f.close()
	lex.input(pf)
	while True:
		tok = lex.token()
		if not tok: break
		print (str(tok.type) + ' < ' + str(tok.value) + ' >')