import random

'''
valor = int(input('Digite um valor de 0 a 10 : '))

tupla = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')

print(f'O valor digitado foi : {tupla[valor]}')
'''
lista=[]
cont = 1
while cont<=5 :
    aleatorio = random.randint(0,1000)
    cont+=1
#    print(aleatorio)
    lista.append(aleatorio)
    
lista.sort()
print(lista)