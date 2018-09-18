print('Converta metros em centimetros. ')

print('Escreva a quantidade em metros a ser convertida\n'
      'Digite apenas números inteiros.\n'
      'Em caso de números decimais, use ponto no lugar da vírgula.')

n1 = (float(input('Quantidade em metros: ')))
print('{}m'.format(n1))

cm = n1 * 100
mm  = n1 * 1000

print('{}m = {}cm..'.format(n1,cm))
print('{}m = {}mm..'.format(n1,mm))
