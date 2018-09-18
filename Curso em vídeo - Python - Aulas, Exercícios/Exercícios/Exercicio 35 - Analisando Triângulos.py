### Definindo as variáveis

a = float(input('Digite um primeiro valor: '))
b = float(input('Digite um segundo valor: '))
c = float(input('Digite um terceiro valor: '))


### Calculando a base

base = a
if b>a and b>c:
	base = b

if c>a and c>b:
	base = c

### Se 'a' for o maior, ele continuara sendo a base.
### Se 'b' for o maior valor ele será a base
### Se 'c' for o maior valor ele será a base

### Se 'a' for a base:
### b + c = lados


if a == base:
    lado1 = b
    lado2 = c

if b == base:
	lado1 = a
	lado2 = c

if c == base:
	lado1 = a
	lado2 = b


print('A base é igual à {:.2f}'.format(base))
print('O lado esquerdo é igual à: {:.2f}'.format(lado1))
print('O lado direito é igual à: {:.2f}'.format(lado2))

if lado1 + lado2 > base:
    print('Uau! Com essas linhas você consege fazer um triângulo!!! ')
else:
    print('Oh não! Parece que essas linhas são muito pequenas para fazer um triângulo! ')

print('- Fim do Programa -')