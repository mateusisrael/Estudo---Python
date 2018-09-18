# ESTRUTURA DE REPETIÇÃO CRIADA COM WHILE E FOR
# 9 de março de 2018


from time import sleep

x = 0

while x < 5:
    x = x + 1
    print(x)
    sleep(1)


    if x == 5:
        x = 0
        print('\n'
              '===============\n'
              'Recomeçando em:\n'
              '===============')

        for c in range(3, 0, -1):
            print(c, '---------')
            sleep(1)

        print('\n'
              'Já:')
        sleep(1)