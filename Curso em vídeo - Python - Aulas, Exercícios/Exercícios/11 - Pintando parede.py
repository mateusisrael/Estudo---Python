print('Calcule a quantidade de tinta que você vai precisar para pintar sua parede.')

#Cada lata de tinta pinta 2m quadrados
# M² = comprimento X Largura
input('ATENÇÃO. Digite apenas números a seguir.\n'
      'Para caso de números decimais, use ponto no lugar da vírgula.')

com = (float(input('Digite o comprimento da sua parede: ')))
lar = (float(input('Digite a largura da sua parede: ')))
m2  = com * lar
lit = m2 / 2

print('Sua parede tem {:.2f}m² e você vai precisar de {:.2f} litros de tinta. '.format(m2,lit))

