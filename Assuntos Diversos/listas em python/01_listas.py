'''
Mateus Israel
02 de outubro de 2018
Praticando o uso de listas em python
'''

numeros_impares = ['1', '3', '5', '7', '9']			# Uma lista pode receber diversos dados de diversos tipos
numeros_pares = [2, 4, 6, 8]						# Na lista acima recebemos strings na lista ao lado inteiros

for numero in numeros_impares:		# Para cada numero em numeros_impares (lista)
	print(numero)					# Printar numero. Poderiamos também printar a própria lista

print('')

for numero in numeros_pares:
	print(numero)

print('\nFim da lista!')
