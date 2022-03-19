#Estrutura with --- ARQUIVOS ---

# SEM WITH

# arquivo = open('meuaquivo.txt','w')

# arquivo.write('Escrevendo no aquivo')

# arquivo.close()


# Com With

with open('meuaquivo.txt','w') as arquivo:
    arquivo.write('Escrevendo segunda linha no aquivo')
