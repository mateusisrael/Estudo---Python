# Exercício 45
# Crie um programa que faça o computador jogar jokenpô (pedra,papel,tesoura) com você.
########################################################################################


# ESCOLHA DA MAQUINA
from random import choice
escolha_pc = choice(['pedra', 'papel', 'tesoura'])

print('[1] PEDRA \n'
      '[2] PAPEL \n'
      '[3] TESOURA')

1 = pedra
2 = papel
3 = tesoura

escolha_player = int(input('Digite um número de acordo com sua escolha: '))


#CONDIÇÕES
if escolha_pc == escolha_player:
    print('Escolhi.............{} \n'
          'Você escolheu.......{} \n'
          '***  Parece que empatamos :D !'.format(escolha_pc, escolha_player))

elif escolha_pc == pedra and escolha_player == tesoura:
    print()
elif escolha_pc == tesoura

print(escolha_pc)