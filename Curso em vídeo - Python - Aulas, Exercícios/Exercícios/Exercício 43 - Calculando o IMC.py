# Exercício 43
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
# e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: abaixo do peso
# - Entre 18.5 e 25: peso ideal
# - 25 até 30: sobrepeso
# - 30 até 40: Obesidade mórbida
## O cálculo do IMC é feito dividindo o peso (em quilogramas) pela altura (em metros) ao quadrado.
###############################################################################################################


print('====    Calcule seu IMC    ====\n')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

# imc recebe peso dividido pela altura ao quadrado
imc = peso / (altura ** 2)

print('Seu IMC é: {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do seu peso ideal! ')
elif imc >= 18.5 and  imc <= 24.9:
    print('Você está no seu peso ideal! ')
elif imc >= 25.0 and imc <= 29.9:
    print('Você está com SOBREPESO! ')
elif imc >= 30.0:
    print('Você está com OBESIDADE MÓRBIDA! ')

print('\n'
      '====    Fim do programa!    ==== ')