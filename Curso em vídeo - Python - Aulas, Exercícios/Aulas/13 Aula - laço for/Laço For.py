
from time import sleep

x = str(input('Valor: '))
y = str(input('Valor 2: '))
vzs = int(input('Vezes para aparecer: '))

contagem = 0                                                    # A variável dever ser declarada antes do loop
for c in range(1, vzs+1):
    contagem = contagem + 1
    print('{}º ==============='.format(contagem))
    print(x)
    print(y, '\n')
    sleep(2)

print('Fim do programa')
