# 15 de maio de 2018, Mateus
# Tocando mp3 com algumas condições, de forma que possa ser usado em joguinhos e outras ultilidades
# A ideia desse programa é fazer o computador escolher um número com o módulo choice.
# Se o número escolhido pelo pc for maior que o digitado no input, o computador ganha e aparece uma mensagem
# dizendo que o player perdeu com uma musiquinha de derrota, se o player escolher 

# Módulos ultilizados nesse programa
from playsound import playsound
from random import choice
from time import sleep

x = int(input('Digite um valor entre 1 e 10: '))
y = int(choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']))
sleep(2)
print('\n'
      'Sua escolha:   {}\n'
      'Escolha do PC: {}'.format(x, y))
sleep(2)
if x == y:
    print('>>> Empate <<<')
elif x > y:
    print('>> Você Venceu <<')
    playsound('vitoria.m4a')
elif x < y:
    print('>> Você Perdeu <<')
    playsound('derrota.m4a')

print('\n'
      'Fim de jogo!')

