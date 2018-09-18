# Parametrô é uma variável declarada entre os parêntesis de uma função e tem seu uso exclusivo dentro da mesma.
# Sempre que chamarmos a função será obrigatório passar um dado especifico para cada parâmetro que foi declarado.


def soma(x, y):
    total = x + y
    print("O valor total é: {}+{}={}".format(x, y, total))

soma(1, 1)