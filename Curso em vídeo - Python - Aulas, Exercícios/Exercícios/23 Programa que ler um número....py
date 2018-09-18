# Exercício 23
# Faça um programa que leia um número de 0 à 9999 e mostre na tela cada um dos digitos separados>
# 18 de maio de 2018, Mateus

x = (input('Digite um número: '))
tamanho = len(x)                                     # Número de casas recebe tamanho de números de 'x'
print('Casas: {}'.format(tamanho))                   # print números de casas de 'x'

if tamanho == 4:                                     # Se o número for de 4 casas
    x1 = (x[0])
    x2 = (x[1])
    x3 = (x[2])
    x4 = (x[3])
    print('Unidade(s): {}\n'
          'Dezena(s):  {}\n'
          'Centena(s): {}\n'
          'Milhare(s): {}'.format(x4, x3, x2, x1))

elif tamanho == 3:                                  # Se não se o número for de 3 casas
    x1 = (x[0])
    x2 = (x[1])
    x3 = (x[2])
    print('Unidade(s): {}\n'
          'Dezena(s):  {}\n'
          'Centena(s): {}'.format(x3, x2, x1))
elif tamanho == 2:                                  # Se não se o número for de 2 casas
    x1 = (x[0])
    x2 = (x[1])
    print('Unidade(s): {}\n'
          'Dezena(s):  {}'.format(x2, x1))
else:                                               # Se não se o número for de 1 casa
    x1 = (x[0])
    print('Unidade(s): {}'.format(x1))