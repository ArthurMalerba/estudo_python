print('\t ----Tabuada---- ')
numero = int(input('Informe o numero para ver a tabuada: '))

print('### Tabuada de', numero, '###')

for i in range(0, 11):
    print(numero, 'X', i, '=', (numero * i))
