def prioridade(operatores):
    if operatores == '(':
        return 1
    elif operatores == '+' or operatores == '-' or operatores == ".":
        return 2
    elif operatores == '*':
        return 3
    else:
        return 0

def verificaVazia(entrada):
	if entrada == None or entrada == "":
		entrada = "&";
	return entrada

def operandos(xar):
    TodosOperandos = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdrfghijklmnopqrstuvxz'
    return xar.upper() in TodosOperandos

def operadores(xar):
    TodosOperadores = '+-*/.&'
    return xar.upper() in TodosOperadores

print("teste")

#def fixaParaPosFixa():