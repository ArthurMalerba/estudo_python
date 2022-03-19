import datetime

mes_ext = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho','julho','agosto','setembro','outubro','novembro','dezembro']
data = input('Entre com uma data do seu nascimento (DD/MM/YYYY) : ')

dia,mes,ano = data.split("/")

print (f"Você nasceu em {dia} de {mes_ext[int(mes)-1]} de {ano}")