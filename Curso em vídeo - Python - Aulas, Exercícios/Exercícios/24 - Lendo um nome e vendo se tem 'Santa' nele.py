# Exercicio 24 - Crie um programa que leia um nome e diga se ele começa ou não com 'SANTO'.
# 18 de maio de 2018, Mateus

nome = str(input('Nome: ')).upper()
separa = (nome.split())
santo = (separa[0])
print(santo)
if santo == 'SANTO':
    print('Esse nome começa com "Santo"')
else:
    print('Esse nome não começa com "Santo"')
