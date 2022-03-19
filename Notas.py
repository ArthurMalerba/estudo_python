'''
Programa para gerar média de notas de um aluno
'''

nota1 = float(input('Entre com a nota 1 (de 0 a 10) : '))
nota2 = float(input('Entre com a nota 2 (de 0 a 10) : '))
nota3 = float(input('Entre com a nota 3 (de 0 a 10) : '))

media = (nota1 + nota2 + nota3) / 3

aprovacao = ''

if media >= 6.0:
    aprovacao = 'Aprovado'
else :
    aprovacao = 'Em recuperação'

print(f'Sua Média final foi : {round(media,2)} sendo assim seu Status é : <<<{aprovacao}>>>.')
