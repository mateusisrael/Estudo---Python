# Declaração dos cães
# 8 de maio de 2018, Mateus

print('Você está prestes a ler a Declaração dos Cães!')
print('[1] Para continuar\n'
      '[2] Para sair\n')
x = int(input('>> '))

if x == 1:
    print('========================================================================================================\n')
    declaracao = open('declaração_dos_cachorros.txt','r')
    for linha in declaracao:
        linha = linha.rstrip()
        print(linha)
    declaracao.close()
    print('\n\n========================================================================================================\n')

