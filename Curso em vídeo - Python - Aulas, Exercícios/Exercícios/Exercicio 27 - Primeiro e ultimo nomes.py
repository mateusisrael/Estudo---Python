# Exercicio 27: Crie um programa que leia o nome completo de uma pesssoa, mostrando em seguida o primeiro e o
# ultimo nome de uma pessoa

nome = str(input('Nome: ')).strip().upper()
nomes = nome.split()
ultimo_nome = len(nomes)                                        # Variável que vai definir a quantidade de nomes

print(' ')
print('Seu nome completo:   {}'.format(nome))
print('Seu primeiro nome é: {}'.format(nomes[0]))
print('Seu último nome é:   {}'.format(nomes[ultimo_nome-1]))  # Quantidade de nomes - 1

print('\n'
      'Fim do programa!'
      '\n')

