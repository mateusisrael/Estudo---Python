# faça um program que leia o preço de um produto e mostre seu novo preço com 5% de desconto

val = (float(input('Digite o valor do produto.\n'
                   'Em caso de números decimais, use ponto ao invés de vígula.\n'
                   'R$')))

des = val * (95/100)

print('O valor do produto é R${:.2f},\n'
      'com desconto o valor cai para R${:.2f}.'.format(val,des))