# Desenvolva um programa que pergunte a distância de uma viagem em km,
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km e
# R$0,45 para viagens mais longas.

distancia = float(input('Digite a distância da sua viagem(ex: xx.xx:): km'))

if  distancia<=200.00:
    val = distancia*0.50
else:
    val = distancia*0.45

print('Valor de sua passagem:\n'
      '\n'
      '======  R${:.2f}  ====== '.format(val))
