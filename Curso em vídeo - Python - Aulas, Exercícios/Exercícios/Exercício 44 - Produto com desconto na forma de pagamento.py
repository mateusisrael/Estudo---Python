# Exercício 44
# Elabore um programa que calcule o valor a ser pago por um produto, considerando
# o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque:  10 por cento de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
####################################################################################


# DEFININDO O VALOR DO PRODUTO
print('Preço do produto')
valor = float(input('R$: '))

print('=== Forma de pagamento ===')

print('[1] À vista.................10% de desconto\n'
      '[2] À vista no cartão.......5% de desconto\n'
      '[3] Em até 2x no cartão.....Sem desconto\n'
      '[4] 3x ou mais no cartão....20% de juros\n')


# ESCOLHENDO A FORMA DE PAGAMENTO
escolha = int(input('Escolha um número da lista de acordo\n'
                    'com a forma de pagamento desejada: \n-> '))


# CONDIÇÕES:
if escolha == 1:
    nvalor = (10/100) * valor
    print('Valor do produto..........................R${:.2f} \n'
          'Novo valor com desconto de 10%............R${:.2f} '.format(valor, nvalor))


elif escolha == 2:
    nvalor = valor - (5/100) * valor
    print('Valor do produto..........................R${:.2f} \n'
          'Novo valor com desconto de 5%.............R${:.2f} '.format(valor, nvalor))

elif escolha == 3:
    nvalor = valor / 2
    print('Valor do produto..........................R${:.2f} \n'
          'Dividido em 2 parcelas de.................R${:.2f} '.format(valor, nvalor))

elif escolha == 4:
    nvalor = (120/100) * valor
    pvalor = nvalor / 3
    print('Valor do produto..........................R${:.2f} \n'
          'Valor parcelado em 3x (20% de juros)......R${:.2f} \n'
          'Com 3 parcelas de.........................R${:.2f}'.format(valor, nvalor, pvalor))


else:
    print('Opção inválida! Por favor tente novamente! ')


#FINALIZANDO
print('Fim do programa === ')