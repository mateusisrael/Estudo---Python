# Para abrir um arquivo ele deve estar na mesma pasta, se não será necessário informar
# todo o  caminho do arquivo

pontuações = open('arquivo.txt','r')    # pontuações recebe 'arquivo.txt' ('r' = somente leitura)
for linha in pontuações:                # for(para ler) linha in(em) pontuações(arquivo.txt)
    linha = linha.rstrip()              # linha recebe = linha.rstrip()(para cortar os espaços entre as linhas
    print(linha)                        # print linha
pontuações.close()                      # Fecha pontuações(arquivo.txt)