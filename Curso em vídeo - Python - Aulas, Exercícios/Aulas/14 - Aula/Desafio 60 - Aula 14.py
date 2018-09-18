# Desafio 60, Aula 14
# Mateus, 2 de agosto de 2018

'''Desafio descrição: Faça um programa que leia um número qualquer e mostre seu fatorial:
Exemplo: 5! = 5x4x3x2x1 = 120'''

''' BASE DO CALCULO
from time import sleep
num = 5

while num != 1:
    result = num * (num-1)
    num = num - 1
    sleep(1)
    print(result)'''


from time import sleep
num = 5
num += 1
print(num)
result = 0

while num != 1:
    num = num - 1
    sub = num -1
    print('\n'
          'num = {}'.format(num))

    multiplicacao = num * sub
    sleep(1)

    print('resultado da multi: {}X{}={}'.format(num, sub, multiplicacao))


    #result = result + multiplicacao
    print('result total: {}'.format(result))
    sleep(3)


print('\n'
      'FIM DO PROGRAMA! ==========')
