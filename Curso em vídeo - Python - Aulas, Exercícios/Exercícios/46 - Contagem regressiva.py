# 14 de junho de 2018

from time import sleep

print('Contagem regressiva!')
input('Para iniciar, pressione ENTER')
print('')

for contagem in range(10, 0, -1):
    print(contagem)
    sleep(1)
print('   Cronômetro zerado!   ')
print('\n'
      'Fim do programa')