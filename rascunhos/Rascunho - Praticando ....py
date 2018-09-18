from time import sleep

print('=== Cronômetro ===')
numero = int(input('Valor: '))

for x in range(numero, 0):
    print(numero)
    numero = numero - 1
    sleep(1)

print('\n'
      'Cronômetro Zerado')