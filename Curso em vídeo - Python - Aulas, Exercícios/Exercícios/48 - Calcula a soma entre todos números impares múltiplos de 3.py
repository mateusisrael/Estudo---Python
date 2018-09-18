# Exercício 48
# Faça um programa que calcule a soma entre todos os números impares que são múltiplos
# de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for num in range(1, 501, 2):                        # Números de 1 a 500 pulando de 1 em 1 (só os números pares)
    if num % 3 == 0:                                # Se o result de num dividido por 3 for igual a 0
        soma = soma + num                           # Soma recebe soma + o número da variável num
        cont = cont + 1                             # cont recebe cont + 1

print('\n'
      'A soma de todos os {} valores impares múltiplos de 3 é {}.'.format(cont, soma))
