# Exercício 26: Programa que lê uma frase pelo teclado e mostre:
# - Quantas vezes a letra 'a' aparece.
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase frase: ')).strip()

a_nafrase = frase.count('a')                                # Quantas vzs o 'a' aparece na frase
posicao1 = frase.find('a') + 1
posicao2 = frase.rfind('a') + 1

print('='*50)
print('Sua frase tem {} letra(s) "a".'.format(a_nafrase))
print('A primeira letra "a" aparece na {}ª posição'.format(posicao1))
print('A última letra "a" aparece na {}ª posição.'.format(posicao2))
