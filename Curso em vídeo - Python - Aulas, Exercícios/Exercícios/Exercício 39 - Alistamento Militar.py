# Faça um programa que leia o ano de nascimento de um jovem e informe, de
# acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é hora de se alistar.
# - Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('\nDigite sua idade para saber quando você deve fazer o alistamento militar:\n\n '))


if idade < 18:
    x = 18 - idade
    print('\n'
          'Você ainda é muito novo para se alistar!\n'
          'Volte daqui à {} ano(s)! '.format(x))

elif idade == 18:
    print('\n'
          'Você deve se alistar já! ')

else:
    x = idade - 18
    print('\n'
          'Você deveria ter se alistado a {} ano(s) atrás! '.format(x))

print('Fim do Programa! ')