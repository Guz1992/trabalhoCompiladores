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


#def fixaParaPosFixa():