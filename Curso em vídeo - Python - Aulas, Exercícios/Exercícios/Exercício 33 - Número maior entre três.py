# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

# Calculando o maior valor:
maior = 0
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

#Calculando o menor valor:
menor = 0
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

# Imprimindo o resultado:
print('O maior valor é:\n'
      '====  {} ====\n'.format(maior))

print('O menor valor é:\n'
      '==== {} ====\n'.format(menor))
