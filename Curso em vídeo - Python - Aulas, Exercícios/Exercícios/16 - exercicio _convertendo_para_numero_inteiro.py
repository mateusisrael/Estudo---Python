# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# EX: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.
#####


import math

num = float(input('Digite um valor: '))

print('O número {} inteiro é {}'.format(num, math.trunc(num)))
