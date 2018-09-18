# Exercício 49
# Refaça o exercicio 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço 'for'.
# 16 de março de 2018


print('==========================\n'
      '    Tabuada de Adição\n'
      '==========================')

from time import sleep
sleep(1)

n1 = int(input('Digite um número: '))
print('')

for c in range(0, 10):
    sleep(1)
    n2 = n1 + c
    print('.......... {}+{}={}'.format(c, n1, n2))

print('\nFim ======================')