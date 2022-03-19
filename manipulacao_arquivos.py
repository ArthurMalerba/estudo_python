def arquivos (tipo,caminho,conteudo):

    #abrindo arquivos
    with open(caminho,tipo) as arq:

        if tipo=='r':
            # Leitura de dados em Arquivos
            print(arq.read())
        elif tipo == 'w':
            #Gravação de Dados em Arquivos
            arq.write(conteudo+"\n")
        else:
            csprint('Erro ao gerar')

    


arquivos('a','arquivo1.txt','123444')

