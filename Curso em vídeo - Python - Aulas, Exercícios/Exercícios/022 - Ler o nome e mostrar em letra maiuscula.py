# 09 de maio de 2018, Mateus
# Exercício 22
# - Crie um programa que leia o nome completo de uma pessoa e mostre:
#	O nome com todas as letras maiúsculas
#	O nome com todas as letras minúsculas
#	Quantas letras ao todo (sem considerar espaços)
#	Quantas letras tem o primeiro nome


nome = str(input('Nome completo: ')).strip()                                                 # .strip() serve para eliminar os
                                                                                    # espaços no começo e fim da string

print('1 - Analisando seu nome...')
print('2 - Seu nome em maiúsculas: {}'.format(nome.upper()))
print('3 - Seu nome em minúsculas: {}'.format(nome.lower()))

print('4 - Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))    # operador -(menos) para remover os espaços no meio da frase
print('5 - Seu primeiro nome tem {} letras.'.format(nome.find(' ')))                # definindo quantas letras tem o primeiro nome, de acordo
                                                                                    # com o primeiro espaço encontrado

separa = nome.split()
print('\n'
      '6 - Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))   # o comando .split() cria uma lista com os elementos na
                                                                                        # frase. A maneira de 'chamar' os elementos separados
                                                                                        # é com os números... 0 = primeiro_nome 1 = segundo_nome...