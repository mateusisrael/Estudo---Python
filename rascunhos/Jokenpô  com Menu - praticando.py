# Jokenpô (pedra, papel, tesoura)
# 10 de março de 2018


print('===============    Jokenpô    ===============')
from random import choice
a = choice(["PEDRA", "PAPEL", "TESOURA"])
PEDRA = 1
PAPEL = 2
TESOURA = 3

print('\n'
      'Pedra, Papel ou Tesoura?\n'
      ' [1] ---- PEDRA\n'
      ' [2] ---- PAPEL\n'
      ' [3] ---- TESOURA\n')
b = int(input('=> '))

if b != 1 or 2 or 3:
    print('Valor inválido! Digite outro valor:\n')
    print('\n'
          'Pedra, Papel ou Tesoura?\n'
          ' [1] ---- PEDRA\n'
          ' [2] ---- PAPEL\n'
          ' [3] ---- TESOURA\n')
    b = int(input('=> '))

    if b == 1 or 2 or 3:
        if a == b:
            print('Parece que empatamos! ')