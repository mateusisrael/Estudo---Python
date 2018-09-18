# 8 de maio de 2018, Mateus
palavra = str(input('Digite aqui a palavra a ser escrita: '))

## Escrevendo no arquivo #####
arquivo = open('arquivotexto.txt','a')
arquivo.write('\n{}'.format(palavra))
arquivo.close()


## Lendo o arquivo de texto
arquivo = open('arquivotexto.txt','r')
print('')
print(arquivo.read())
arquivo.close()

## Finalizando o programa #####
print('\n======================================================\nFim do programa')