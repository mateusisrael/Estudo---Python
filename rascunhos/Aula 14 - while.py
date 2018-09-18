# Curso em vídeo: Aula 14. 31 de julho de 2018
# Mateus
# Estrutura de repetĩção while

# A diferença básica do for para o while é que
# o for geralmente é usado quando você sabe o
# limite de repetições que vc quer usar.
# Já o while não tem um limite definido.

# Exemplo prático:

n = 1
par = impar = 0
while n != 0:
	n = int(input('Digite um valor: '))
	if n != 0:
		if n % 2 == 0:
			par += 1
		else:
			impar += 1
print('\n'
	 'Você digitou {} números pares e {} números ímpares!'. format(par, impar))