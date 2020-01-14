from time import sleep

arq = open("Page1-1000_PdfToWord.txt", "r")

while True:
    conteudo1 = arq.readline()
    

    #Primeira etapa é encontrar o Nome:
    while True:
       
        #Encontrando nome
        if conteudo1.find('Nome:') != -1:
            print(f"Len {len(conteudo1[5:])} {conteudo1[5:]}" )
            sleep(2)
            
            if len(conteudo1[5:]) == 1:
                
                #Ideia 1 nome abaixo
                print(">",conteudo1[5:])
                conteudo1 = arq.readline()
                if conteudo1.find('Nascimento:') == 0:
                    print(conteudo1.find('Nascimento:'))
                    conteudo1 = arq.readline()
                    conteudo1 = arq.readline()
            conteudo2 = arq.readline()
            break
        
        else:
            conteudo1 = arq.readline()    


    #Segunda etapa é encontrar o numero e associar com o nome
    while True:
        
        
        #Encontrando numero
        if conteudo2.find('Telefones:') != -1:
            conteudo2 = arq.readline()
            conteudo2 = arq.readline()
            
            break
        
        else:
            conteudo2 = arq.readline()
        
    #print(f'Nome: {conteudo1[6:]}Telefone: {conteudo2}')   
               
            
        
        
        
    
# ++++Ideias++++  

# Nome geralmente esta a uma linha abaixo
# Nome geralmente esta 3 linhas abaixo

# xxxx+Problemas+xxxx

# Linhas em branco
# Nao nomes    



