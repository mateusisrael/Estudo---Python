                                                                # Escolhendo uma das opções
print('[1] Ver fotos\n'
      '[2] Sair'
      '')
x = int(input('Escolha uma das opções acima: '))
if x == 1:
    print('\n'
          'Vendo fotos\n'
          '###########')

if x == 2:
    print('\n'
          'Finalizando...')

print('\n'
      '===============\n'
      'Fim do programa\n'
      '===============')
while x != 1 and x != 2:
    print('\n'
          'Valor Inválido')
    x = int(input('Escolha uma das opções acima: '))