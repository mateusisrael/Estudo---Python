'''
Mateus Israel
02 de outubro de 2018
Praticando o uso de listas em python
'''


'''
Métodos das listas

append()
O primeiro método a ser analisado é o append(), que tem por objetivo adicionar um novo elemento no final da lista.

insert()
Caso desejemos fazer essa inserção em uma posição específica, podemos utilizar o método insert() que,
além do elemento a ser inserido, recebe também o índice que ele deve assumir

pop()
remove o último item da lista e o retorna como resultado da operação. Caso seja necessário remover
um índice específico, basta informá-lo como argumento.

remove()
Nos dois casos, a remoção foi feita com base na posição do objeto, porém, há situações em que esse
índice é desconhecido e desejamos remover o item a partir do seu valor. Para isso temos o método remove(item)

sort()
ordena a lista.

reverse()
inverte as posições dos itens.

count()
retorna o número de ocorrências de determinado objeto, passado como parâmetro


Sintaxe:
	lista.metodo()
	lista.metodo(parametro, objeto_ou_indice)