# Escreva um programa que faça o computador "pensar" em um número inteiro entre
# 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
x = random.randrange(5)
y = int(input('Digite um número de 0 à 5: '))

if x==y:
    print('Parabéns você acertou!! ')

else:
    print('Você perdeu! ')

print('')
print('Número sorteado: {}.\n'
      'Você digitou: {}. '.format(x,y))