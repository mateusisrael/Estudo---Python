# 9 de maio, Mateus
# Agenda que lê adiciona e remove contatos. ============================================================================


from time import sleep
# Criando arquivo txt (se ainda não o tiver criado) ====================================================================
# txt = open("agenda.txt",'x')
# txt.close()


# Menu de opções =======================================================================================================
print('Opções:\n'
      '[1] Adicionar contatos\n'
      '[2] Ver lista de contatos\n'
      '[0] Sair')

menu_opcao = int(input('Escolha uma das opções acima: '))

# Loop de opção inexistente
while menu_opcao < 1 or menu_opcao > 4:
    print('Opções:\n'
          '[1] Adicionar contatos\n'
          '[2] Ver lista de contatos\n'
          '[0] Sair')

    menu_opcao = int(input('Escolha uma das opções acima: '))
# ======================================================================================================================


# Condições
# Adicionando contatos à agenda ========================================================================================

if menu_opcao == 1:
    print('==================================================================================')
    contato = str(input('Escreva o nome e o número do seu novo contato.\n'
                        '>> '))
    print('==================================================================================')
# ======================================================================================================================


    # Abrindo o arquivo txt e adicionando o contato ====================================================================
    txt = open('agenda.txt','a')
    txt.write('\n{}'.format(contato))
    txt.close()

    print('\nAdicionando...')
    sleep(2)
    print('Contato salvo com sucesso!!!')
# ======================================================================================================================


# ======================================================================================================================
if menu_opcao == 2:
    txt = open('agenda.txt','r')
    print('\n==================================================================================\n'
          'Contatos Salvos na lista')
    print(txt.read())
    print('==================================================================================')
    txt.close()
    input('Pressione Enter para continuar\n'
          '')
# ======================================================================================================================


# "Rebobinando" o programa
# Menu de opções =======================================================================================================
print('Opções:\n'
      '[1] Adicionar contatos\n'
      '[2] Ver lista de contatos\n'
      '[0] Sair')

menu_opcao = int(input('Escolha uma das opções acima: '))

# Loop de opção inexistente
while menu_opcao < 1 or menu_opcao > 4:
    print('\n'
          '\nOpções:\n'
          '[1] Adicionar contatos\n'
          '[2] Ver lista de contatos\n'
          '[0] Sair')

    menu_opcao = int(input('Escolha uma das opções acima: '))
# ======================================================================================================================