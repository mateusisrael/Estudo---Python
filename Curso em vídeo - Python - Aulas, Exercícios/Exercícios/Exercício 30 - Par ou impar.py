# Crie um programa que leia um número inteiro e mostre na tela se ele é
# par ou impar.
num = int(input('Digite um número: '))

# O segredo desse programa está nesse calculo "cal=num%2"!
# "Você precisa usar um operador chamado modulo, pois ele fará a divisão do numero, e te retornara
# o resto, dessa forma se um numero divido por 2 retornar zero, ele será par caso contrário ele será impar."
cal = num%2

if cal==0:
    print('O número digitado é par! ')
else:
    print('O número digitado é impar! ')