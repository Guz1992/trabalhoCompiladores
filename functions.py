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
	base.Transicoes.append(0)
	base.Transicoes.append(1)
	base.Transicoes.append(simbolo)
	base.estadoInicial = 0
	base.estadosFinal = 1
	return base


def uneAlfabetos(a,b):
	return a+b

def distibuiChars(lista,lista2):
	for i in range(0,len(lista)):
		lista2.append(lista[i])
	return lista2	

def fechoDeKleene(Ak):
	novo = Automato()
	novo.alfabeto = uneAlfabetos(Ak.alfabeto,"")
	novo.qtEstados = Ak.qtEstados+2
	novo.estados = [None]*novo.qtEstados
	
	for i in range(0,len(novo.estados)):
		novo.estados[i] = i
	
	novo.Transicoes.append([Ak.Transicoes[0],Ak.Transicoes[1],Ak.Transicoes[2]])
	novo.Transicoes.append([novo.estados[0],novo.estados[-1],"&"])
	novo.Transicoes.append([novo.estados[0],Ak.Transicoes[0],"&"])
	novo.Transicoes.append([Ak.Transicoes[-2],novo.estados[-1],"&"])
	novo.Transicoes.append([novo.estados[-1]-1,novo.estados[0]+1,"&"])

	novo.estadoInicial = 0
	novo.estadosFinal = novo.estados[-1]

	return novo

def concatenacao(A,B):
	novo = Automato()
	novo.alfabeto = uneAlfabetos(A.alfabeto,B.alfabeto)
	novo.qtEstados = A.qtEstados+B.qtEstados
	novo.estados = [None]*novo.qtEstados
	
	for i in range(0,len(novo.estados)):
		novo.estados[i] = i
	
	novo.Transicoes.append([A.Transicoes[0],A.Transicoes[1],A.Transicoes[2]])
	novo.Transicoes.append([B.Transicoes[0],B.Transicoes[1],B.Transicoes[2]])
	novo.Transicoes.append([A.Transicoes[-2],B.Transicoes[0],"&"])

	novo.estadoInicial = 0
	novo.estadosFinal = novo.estados[-1]

	return novo

def uniao(A,B):
	novo = Automato()
	novo.alfabeto = uneAlfabetos(A.alfabeto,B.alfabeto)
	novo.qtEstados = A.qtEstados+B.qtEstados+2
	novo.estados = [None]*novo.qtEstados
	
	for i in range(0,len(novo.estados)):
		novo.estados[i] = i
	
	novo.Transicoes.append([A.Transicoes[0],A.Transicoes[1],A.Transicoes[2]])
	novo.Transicoes.append([B.Transicoes[0],B.Transicoes[1],B.Transicoes[2]])
	novo.Transicoes.append([novo.Transicoes[0][0],B.Transicoes[0],"&"])
	novo.Transicoes.append([novo.Transicoes[0][0],A.Transicoes[0],"&"])
	novo.Transicoes.append([A.Transicoes[-2],novo.Transicoes[0][-2],"&"])
	novo.Transicoes.append([B.Transicoes[-2],novo.Transicoes[0][-2],"&"])

	novo.estadoInicial = 0
	novo.estadosFinal = novo.estados[-1]

	return novo

def percorreExpressao(expressao):
	pilha = []
	for i in range(0,len(expressao)):
		if operandos(expressao[i]):
			pilha.append(baseF(expressao[i]))
		elif operadores(expressao[i]):
			if(expressao[i] == "*"):
				op1 = pilha.pop(-1)
				pilha.append(fechoDeKleene(op1))
			else:
				op2 = pilha.pop(-1)
				if pilha:
					op1 = pilha.pop(-1)
					if expressao[i]== ".":
						pilha.append(concatenacao(op1,op2))
					elif expressao[i] == "+":
						pilha.append(uniao(op1,op2))
	return pilha

def olhaPilha(pilha):
	tudo = []
	for i in range(0,len(pilha)):
		todasT = pilha[i].Transicoes

	for j in range(0,len(todasT)):
		for x in range(0,len(todasT[i])):
			tudo.append(todasT[j][x])

	return tudo