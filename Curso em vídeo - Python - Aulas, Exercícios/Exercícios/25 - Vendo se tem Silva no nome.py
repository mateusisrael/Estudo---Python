# Exercicio 25: Crie um programa que leia um nome e diga se tem 'Silva'
# 18 de maio de 2018, Mateus

nome = str(input('Nome: ')).upper()
silva = nome.find('SILVA')

if silva == -1:
    print('Esse nome não tem "Silva".')

else:
    print('Esse nome tem "Silva".')
