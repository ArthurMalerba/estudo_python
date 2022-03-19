'''
IMC - indice de massa corporal

IMC é a sigla para Índice de Massa Corporal que serve para avaliar o peso do indivíduo em relação à sua altura e assim indicar se está dentro do peso ideal, acima ou abaixo do peso desejado. O cálculo do IMC deve ser feito usando a seguinte fórmula matemática: Peso ÷ altura x altura.

IMC	Classificação do IMC
< 16	Magreza grave
16 a < 17	Magreza moderada
17 a < 18,5 	Magreza leve
18,5 a < 25	Saudável
25 a < 30  	Sobrepeso
30 a < 35 	Obesidade Grau I
35 a < 40  	Obesidade Grau II (severa)
> 40 	Obesidade Grau III (mórbida)


'''
try:
    peso = float(input('Favor digitar o seu Peso :'))
    altura = float(input('Favor digitar a sua Altura :'))

    resultado = peso / (altura * altura)
    
    if resultado < 16:
        print ("Magreza grave")
    elif resultado > 16 and resultado < 17 :
        print ("Magreza moderada")
    elif resultado >= 17 and resultado < 18.1085 :
        print ("Magreza leve")
    elif resultado >= 18.5 and resultado < 25 :
        print (f"{resultado} - Saudável")
    elif resultado >= 25 and resultado < 30 :
        print (f"{resultado} - Sobrepeso")
    elif resultado >= 30 and resultado < 35 :
        print (f"{resultado} - Obesidade Grau I")
    elif resultado >= 35 and resultado < 40 :
        print (f"{resultado} - Obesidade Grau II (severa)")
    elif resultado >= 40  :
        print (f"{resultado} - Obesidade Grau III (Mórbida) ")
except:
    pass

    