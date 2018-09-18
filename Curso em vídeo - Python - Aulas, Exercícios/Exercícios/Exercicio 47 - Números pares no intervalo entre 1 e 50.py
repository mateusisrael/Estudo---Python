# Exercício 47
# Crie um programa que mostre na tela todos os números pares que estão no intervalo
# entre 1 e 50
# 10 de março de 2018

input('Números pares de 0 à 50 (pressione "enter" para continuar): ')
from time import sleep

for x in range(0, 51, 2):
    print('--------- ',x,' ---------')
    sleep(0.5)