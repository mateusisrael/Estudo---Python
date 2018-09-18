print('======= Cronômetro =======')
numero = int(input('Segundos: '))+1

from time import sleep

for x in range(0, numero):
    numero = numero -1
    print(numero)
    sleep(1)

print ('\n'
       '=== Cronômetro zerado ==='
       '\n')