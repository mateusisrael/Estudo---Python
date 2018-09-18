# Faça um algoritmo que leia o salário de um funcionário e  mostre seu novo salário com 15% de aumento.
print('Calcule quanto ficará o salário de seu funcionário com um aumento de 15%.')
salario = (float(input('ATENÇÃO. Digite apenas números,\n'
                       'em caso de números decimais use ponto ao invés de vírgula.\n'
                       'Digite o atual salário do funcionário.\n'
                       'R$')))

aumento = salario * (115/100)

print('O atual salário do fucionário é R${:.2f}. Com o aumento o salário passa a ser\n'
      'R${:=<20.2f}'.format(salario,aumento))