# Relembrando conceitos básicos de programação - 27 de julho de 2018
# Mateus Israel

from time import sleep

nome = str(input("Olá qual seu nome? "))
sleep(1)

print("Olá {}!".format(nome))

idade = int(input("Quantos anos você tem? "))
sleep(1)

if idade >= 18:
    print("Uauu, você já é maior de idade! ")
    sleep(2)
    print('')
    print('Por favor digite seu endereço:')
    endereço = (str(input('Endereço: ')))

    sleep(2)
    print('Seu nome é {}, você tem {} anos e mora em {}!'.format(nome, idade, endereço))
else:
    print('\n'
          'Uau, você é muito jovem para se cadastar em nossos serviços! ')
