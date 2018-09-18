# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('Bem vindo ao contador.\n'
      'O valor do alugueu é: R$60 por dia + R$0.15 por cada quilômetro rodado.'
      'A seguir, digite oque se pede. Use apenas números.\n'
      'Em caso de números decimais, use ponto ao invés de vírgula.')

km =  (float(input('Digite quantos quilômetros você percorreu com o carro alugado. km: ')))
dia = (int(input('Digite quantos dias você alugou o carro. Dias: ')))

#1 km =  RS0.15
#1 dia = RS60.00
tot = (0.15 * km) + (60 * dia)


print('Você percorreu {:.1f}km em {} dia(s) com o carro.\n'
      'O valor a ser pago é: R${:.2f}'.format(km, dia, tot))

