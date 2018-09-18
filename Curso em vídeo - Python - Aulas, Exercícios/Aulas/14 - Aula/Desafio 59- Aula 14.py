# Desafio 59 - Aula 14
# Mateus, 1 de agosto de 2018

# 59:
# Crie um programa que leia dois valores e mostre na tela:

#[1] Somar
#[2] Multiplicar
#[3] Maior
#[4] Novos Números
#[5] Sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
n1 = int
n2 = int
decisao = 4

while decisao != 5:
    if decisao == 1:
        resultado = n1 + n2
        print('\n', resultado)
        sleep(2)
        print('\n'
              '=======================\n'
              'MENU DE SELEÇÃO')
        print('=======================\n'
              '[1] Somar\n'
              '[2] Multiplicar\n'
              '[3] Maior entre eles\n'
              '[4] Novos números\n'
              '[5] Sair do programa\n'
              '=======================')
        decisao = int(input('Escolha: '))
    if decisao == 2:
        resultado = n1 * n2
        print('\n', n1,'X',n2,'=',resultado)
        sleep(2)
        print('\n'
              '=======================\n'
              'MENU DE SELEÇÃO')
        print('=======================\n'
              '[1] Somar\n'
              '[2] Multiplicar\n'
              '[3] Maior entre eles\n'
              '[4] Novos números\n'
              '[5] Sair do programa\n'
              '=======================')
        decisao = int(input('Escolha: '))
    if decisao == 3:
        if n1 > n2:
            print('\n{} é maior que {}.'.format(n1, n2))
        else:
            print('\n{} é maior que {}.'.format(n2, n1))
        sleep(2)
        print('\n'
              '=======================\n'
              'MENU DE SELEÇÃO')
        print('=======================\n'
              '[1] Somar\n'
              '[2] Multiplicar\n'
              '[3] Maior entre eles\n'
              '[4] Novos números\n'
              '[5] Sair do programa\n'
              '=======================')
        decisao = int(input('Escolha: '))
    if decisao == 4:
        print('Calcule: ')
        n1 = int(input('Valor 1: '))
        n2 = int(input('Valor2: '))
        print('\n'
              '=======================\n'
              'MENU DE SELEÇÃO')
        print('=======================\n'
              '[1] Somar\n'
              '[2] Multiplicar\n'
              '[3] Maior entre eles\n'
              '[4] Novos números\n'
              '[5] Sair do programa\n'
              '=======================')
        decisao = int(input('Escolha: '))


print('Finalizando...')