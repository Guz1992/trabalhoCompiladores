""" este código foi desenvolvido pelos alunos, Gustavo Macedo Rodrigues e Idinilson Nunes de Aguiar"""
def precedencia(operatores):
    if operatores == '+' or operatores == "/" or operatores == "-":
        return 1
    elif operatores == ".":
    	return 2
    elif operatores == "*":
        return 3
    elif operatores == '^':
        return 4    
    else:
        return 0

def verificaParenteses(expressao):
	contParenteses = 0
	for i in range(0,len(expressao)):
		if expressao[i] == "(":
			contParenteses += 1
		elif expressao[i] == ")":
			contParenteses -= 1
	return contParenteses		

def verificaVazia(entrada):
	if entrada == None or entrada == "":
		entrada = "&";
	return entrada
	
	expressao = "".join(x)
	return posicoes

def operandos(xar):
    TodosOperandos = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxz&'
    for i in range(0,len(TodosOperandos)):
    	if xar == TodosOperandos[i]:
    		valor = True
    		return True
    	else:
    		valor = False
    return(valor)

def operadores(xar):
    TodosOperadores = '+-*/.^'
    for i in range(0,len(TodosOperadores)):
    	if xar == TodosOperadores[i]:
    		valor = True
    		return True
    	else:
    		valor = False
    return(valor)

def infixaParaPosfixa(expressao):
	posfix = []
	pilha = []
	print(expressao)
	for i in range(0,len(expressao)):
		
		if operandos(expressao[i]):
			posfix.append(expressao[i])
			if(i+1 < len(expressao)):
				if operandos(expressao[i]) and operandos(expressao[i+1]):
					pilha.append(".")	
		elif operadores(expressao[i]):
			
			if not pilha:
				pilha.append(expressao[i])
				if(i+1 < len(expressao)):
					if operandos(expressao[i]) and operandos(expressao[i+1]):
						pilha.append(".")
			elif precedencia(expressao[i])>=precedencia(pilha[-1]):
				pilha.append(expressao[i])
				if(i+1 < len(expressao)):
					if operandos(expressao[i]) and operandos(expressao[i+1]):
						pilha.append(".")
			elif precedencia(expressao[i])<=precedencia(pilha[-1]):
					while pilha:
						if precedencia(expressao[i])<=precedencia(pilha[-1]):
							posfix.append(pilha.pop(-1))
					pilha.append(expressao[i])
		
		elif expressao[i] == "(":
			if(i+1 < len(expressao)):
				if expressao[i] == "(" and operandos(expressao[i+1]):
					pilha.append(".")
			pilha.append(expressao[i])
		elif expressao[i] == ")":
			while operadores(pilha[-1]):
				posfix.append(pilha.pop(-1))
			if pilha[-1] == "(":
				del pilha[-1]
		print(pilha)
				
	while pilha:
		posfix.append(pilha.pop(-1))
		pass			
	return posfix

class Automato(object):
	def __init__(self):
		self.alfabeto = None
		self.estados = None
		self.qtEstados = None
		self.Transicoes = []
		self.estadoInicial = None
		self.estadosFinal = None

def baseF(simbolo):
	base = Automato()
	base.alfabeto = simbolo
	base.qtEstados = 2
	base.estados = [None]*base.qtEstados
	base.estados[0] = 0
	base.estados[1] = 1
	base.Transicoes.append([0,1,simbolo])
	base.estadoInicial = 0
	base.estadosFinal = 1
	return base

def uneAlfabetos(a,b):
	return a+b

def fechoDeKleene(A):
	novo = Automato()
	novo.alfabeto = uneAlfabetos(A.alfabeto,"")
	novo.qtEstados = A.qtEstados+2
	novo.estados = [None]*novo.qtEstados
	
	for i in range(0,len(novo.estados)):
		novo.estados[i] = i

	A.Transicoes[0][0] += 1
	A.Transicoes[0][1] += 1
	
	novo.Transicoes.append(A.Transicoes)
	novo.Transicoes.append([novo.estados[0],novo.estados[-1],"&"])
	novo.Transicoes.append([novo.estados[0],A.Transicoes[0][0],"&"])
	novo.Transicoes.append([A.Transicoes[0][1],novo.estados[-1],"&"])
	novo.Transicoes.append([novo.estados[-1]-1,novo.estados[0]+1,"&"])

	novo.estadoInicial = 0
	novo.estadosFinal = novo.estados[-1]

	print(novo.Transicoes)

	return novo