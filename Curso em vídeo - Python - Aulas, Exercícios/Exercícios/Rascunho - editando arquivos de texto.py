# Treinando a manipulação de arquivos txt
# 11 de maio de 2018, Mateus

from time import sleep                                # IMPORTANDO o módulo de delay
print('Digite aqui seu texto: ')
texto = str(input('>>> ')).strip()

# ESCREVENDO no arquivo de texto ===================
arquivo = open('rascunho.txt', 'w')
arquivo.write('\n {}'.format(texto))
arquivo.close()
#===================================================

print('\nSalvando...\n')                              # INTERAÇÃO com o usuário
sleep(2)                                              # Delay ====================

print('Digite:\n'                                     #===========================
      '[1] Para ler seu arquivo\n'                    # Dando a opção de ler o que
      '[2] Para finalizar o programa')                # foi escrito
escolha = int(input('>>>'))                           #===========================

if escolha == 1:
    # LENDO o arquivo de texto =====================
    arquivo = open('rascunho.txt', 'r')
    print(arquivo.read())
    arquivo.close()
    # ==============================================

print('\n'
      'Finalizando...')                              # FINALIZANDO o programa
sleep(2)                                             # Delay =====================