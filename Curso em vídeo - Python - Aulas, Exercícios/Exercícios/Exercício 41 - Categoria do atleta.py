# Exercício 41
# A confederação nacional de natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - até 9 anos: Mirim
# - até 14 anos: Infantil
# - até 19 anos: Junior
# - até 20 anos: Sênior
# - Acima: Master

x = int(input('Idade: '))

if x <= 9:
    print('Sua categoria é MIRIM!')
elif x <= 14:
    print('Sua categoria é INFANTIL!')
elif x <= 19:
    print('Sua categoria é JUNIOR!')
elif x == 20:
    print('Sua categoria é SÊNIOR!')
else:
    print('Sua categoria é MASTER!')

print('Fim do programa! ')