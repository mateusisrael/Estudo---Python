# 07 de Março de 2018
# Exercício 36:
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantas
# vezes ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
# salário ou então o empréstimo será negado.

valor_casa = float(input('Valor da casa: '))
salario = float(input('Seu salário é: '))
parcelas = float(input('Quantas vezes você deseja parcelar? '))

parcelas = valor_casa / parcelas
porcentagem = salario / (100/30)

print('\n'
      'Valor Mensal: R${:.3f} '.format(parcelas))
print('Porcentagem (30% do seu salário mensal): R${:.3f}\n'.format(porcentagem))

if porcentagem >= parcelas:
    print('\n'
          'Parabéns!!! O emprestimo foi APROVADO!\n'
          '\n'
          'Valor total: R${:.3f} '.format(valor_casa))
    print('Valor mensal das faturas: R${:.3f} '.format(parcelas))

elif porcentagem < parcelas:
    print('O empréstimo foi REPROVADO! ')

from time import sleep
sleep(2)

print('\n'
      '=====    Fim da operação!     =====')