'''
Programa que retorna peso ideal de uma pessoa
105
Homem ou Mulher
'''

try:
    altura = float(input('Favor digitar a sua Altura :'))

    homem = ((72.7*altura) - 58)/100
    mulher = ((62.1*altura) - 44.7)/100

    print(f'De acordo com sua altura ({altura}) o peso ideal para mulher ({round(mulher,2)}) e para homem ({round(homem,2)}).')

except:
    pass