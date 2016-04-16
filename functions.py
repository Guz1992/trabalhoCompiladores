def precedencia(operatores):
    if operatores == '+' or operatores == '-' or operatores == "." or operatores == "/":
        return 1
    elif operatores == "*":
        return 2
    elif operatores == '^':
        return 3    
    else:
        return 0

def verificaVazia(entrada):
	if entrada == None or entrada == "":
		entrada = "&";
	return entrada

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
			print(posfix)		
		elif operadores(expressao[i]):
			
			print(pilha)
			if not pilha:
				pilha.append(expressao[i])
				print(pilha)
			elif precedencia(expressao[i])>=precedencia(pilha[-1]):
				pilha.append(expressao[i])
			elif precedencia(expressao[i]<=precedencia(pilha[-1])):
				while expressao[i]<=precedencia(pilha[-1]):
					posfix.append(pilha.pop(-1))
					pass		
		elif expressao[i] == "(":
			pilha.append(expressao[i])
		elif expressao[i] == ")":
			while operadores(pilha[-1]):
				posfix.append(pilha.pop(-1))
			if pilha[-1] == "(":
				del pilha[-1]	
				
	while pilha:
		posfix.append(pilha.pop(-1))
		pass			
	return posfix


#def fixaParaPosFixa():