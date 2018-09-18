# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

import random
x = random.randrange(200)

y = 80
if x>y:
    vel = x-y
    multa = (x-y)*7

    print('==================================')
    print('{}km/h '.format(x))
    print('{}km/h acima do limite permitido.'.format(vel))
    print('==================================')
    print('')
    print('>>>>>>  Multa de R${:.2f}  <<<<<<<'.format(multa))

else:
    print('==================================\n')
    print('             {}km/h \n'.format(x))
    print('==================================')