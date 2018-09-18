# Desafio 58 - Aula 14
# Mateus, 1 de agosto de 2018

# Exercício 28, relembrando...
# Escreva um programa que faça o computador "pensar" em um número inteiro entre
# 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Melhore o jodo do desafio 28 onde o computador vai 'pensar' em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinha até acertar,
# mostrando quantos palpites foram necessários para vencer.

from random import choice

num_pc = choice([1, 2, 3, 4, 5])            #Escolha do PC

# Chamando as váriaveis...
num_player = 0
contador = 0
# ========================
print('\n'
      '===============================================================================\n'
      'Tente descobrir o número que o computador está pensando (de 1 a 5)!', '\n')

while num_player != num_pc:
    num_player = int(input('Digite um valor: '))
    contador += 1                          # Primeira tentativa considerada.

    if num_pc == num_player:
        print('O pc escolheu {}\n'
              'Você digitou {}'.format(num_pc, num_player))
        print('Você ACERTOU!')
    else:
        print('Você digitou {}'.format(num_player))
        print('Você ERROU!', '\n')
        print('Tente Novamente!')

print('\n'
      'Você acertou na {}ª tentativa'.format(contador))
print('Fim de Jogo!!!')