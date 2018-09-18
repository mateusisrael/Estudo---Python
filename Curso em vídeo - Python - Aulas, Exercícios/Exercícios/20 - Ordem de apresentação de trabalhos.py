# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')

nomes = [a1,a2,a3,a4]
import random
escolhido = random.sample([a1,a2,a3,a4], k=4)
print('A ordem é:\n'
      '>>> {}'.format(escolhido))