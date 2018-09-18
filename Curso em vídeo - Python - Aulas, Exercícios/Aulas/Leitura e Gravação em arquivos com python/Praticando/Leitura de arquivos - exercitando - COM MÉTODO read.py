# Declaração dos cães
# 8 de maio de 2018, Mateus

# Estrutura condicional. Não é necessária para a leitura do arquivo de texto. =========================================
print('Você está prestes a ler a Declaração dos Cães!')
print('[1] Para continuar\n'
      '[2] Para sair\n')
x = int(input('>> '))


if x == 1:

    # Leitura do arquivo de texto =====================================================================================

    print('========================================================================================================\n')
    declaracao = open('declaração_dos_cachorros.txt','r')       # Primeiro abrir o arquivo, definindo uma variavel
                                                                # O 'r' é para especificar a leitura.
    print(declaracao.read())                                    # Imprimir na tela o texto
declaracao.close()                                              # Fechar o arquivo de texto
