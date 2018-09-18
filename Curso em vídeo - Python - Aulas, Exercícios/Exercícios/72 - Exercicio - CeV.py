# 3 de setembro de 2018, Mateus Israel
# Exercicio de python, CeV.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))
while num >= 21 or num < 0:
    num = int(input('Valor Inválido. Digite um número entre 0 e 20: '))


print('Você digitou o valor {}.'.format(numeros[num]))
