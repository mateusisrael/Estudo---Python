ano = int(input('Ano: '))

div_p_4 = ano % 4
div_p_100 = ano % 100
div_p_400 = ano % 400

if div_p_4 == 0 and div_p_100 != 0:
    print('O ano é bissesto! ')
if div_p_4 == 0 and div_p_100 == 0:
    print('O ano não é bissesto! ')

if div_p_4 != 0 and div_p_400 == 0:
    print('O ano é bissesto! ')
if div_p_4 != 0 and div_p_400 != 0:
    print('O ano não é bissesto! ')

print('\n\n===   Fim do programa!!!   ===')