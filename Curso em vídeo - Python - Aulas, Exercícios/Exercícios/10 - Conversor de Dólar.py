#programa que lê quanto dinheiro a pessoa tem e quantos dólares ela pode comprar
#Cálculo R$1,00 = U$$3,27  €3,67

 real  = (float(input('Digite quantos reais vocêtem.\n'
                     'Para números decimais use o ponto no lugar da virgula. R$')))
dolar = real / 3.27
euro  = real / 3.67

print('Com R${:.2f} você pode comprar:\n'
      'U$${:.2f}\n'
      '€{:.2f}'.format(real,dolar,euro))



