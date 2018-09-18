# Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final de acordo com a média atiginda:
# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('O aluno foi reprovado com uma média de {}. '.format(media))

elif media <= 6.9:
    print('O aluno está de recuperção, com uma média {} '.format(media))

else:
    print('O aluno está aprovado, com uma média {}! '.format(media))