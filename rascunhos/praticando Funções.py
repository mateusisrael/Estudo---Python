# 11 de agosto de 2018
# Mateus Israel
# Praticando o uso de funções



# Funções   ============================/


def adi(x, y):
	val = x + y
	return val

def sub(x, y):
	val = x - y
	return val


def multi(x, y):
	val = x * y
	return val

def div(x, y):
	val = x // y
	return val


#======================================/

#==== Entradas e saídas de dados  =====/


a = int(input('Primeiro valor: '))
b = int(input('Segundo valor:  '))


print('''Escolha:
	(1) Somar
	(2) Subtrair
	(3) Multiplicar
	(4) Dividir''')

opc = int(input('$: '))



#=========== Condições ================/


if opc == 1:
	adi(x=a, y=b)
	print('Resultado: {}+{}={}'.format(a, b, adi(a, b)))

elif opc == 2:
	sub(x=a, y=b)
	print('Resultado: {}-{}={}'.format(a,b, sub(a, b)))
	

elif opc == 3:
	multi(x=a, y=b)
	print('Resultado: {}.{}={}'.format(a, b, multi(a, b)))
	

elif opc == 4:
	div(x=a, y=b)
	print('Resultado: {}/{}={}'.format(a, b, div(a, b)))


#=====================================/