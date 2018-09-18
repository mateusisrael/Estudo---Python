# Treinando manipulação de texto
# 11 de maio de 2018, Mateus

print('Digite uma frase: ')
frase = str(input('>>> ')).strip()

print('\n'
      'Sua frase em letras maiúsculas: ')
frase_upper = frase.upper()
print(frase_upper, '\n')

print('\n'
      'Sua frase em letras minúsculas: ')
frase_lower = frase.lower()
print(frase_lower, '\n')

frase_palavras = len(frase) - frase.count(' ')
print('Sua frase tem {} letras no total. \n'.format(frase_palavras))

print('\n'
      'Finalizando...\n'
      '')

palavras = frase.split()
print('A primeira palavra da sua frase é "{}". '.format(palavras[0]))