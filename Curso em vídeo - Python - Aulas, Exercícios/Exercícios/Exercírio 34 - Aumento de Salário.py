# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do
# seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário atual: '))
print('Salário atual: {:.2f}\n'.format(salario))

# Função de 'Pausa(por segundos)'
from time import sleep
sleep(2)

# Tomada de decisão + calculo + impressão:
if salario >= 1250.00:
    nsalario = salario * (110/100)
    print('O novo salário do funcionário, com um aumento de 10% é:'
          '==========   {:.2f}   =========='.format(nsalario))

if salario <= 1249.00:
    nsalario = salario * (115/100)
    print('O novo salário do funcionário com aumento de 15% é:'
          '\n'
          '==========   {:.2f}   =========='.format(nsalario))

print('.\n.'
      '\n.'
      '\n.'
      '\n.'
      '\n'
      '======  Fim do programa  ======')