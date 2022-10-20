def change(dados,virg:str, pontv:str):
    lt_dados = list(dados)     
    flag_aspas = False

    for i in range(len(lt_dados)):            
        if not flag_aspas:
            #Caso haja uma primeira aspa, levanta-se a flag
            if lt_dados[i] == '"':
                flag_aspas = True        
            #As virgulas serao alteradas enquanto a flag estiver desligada
            elif lt_dados[i] == virg:                    
                lt_dados[i] = pontv
        #Ultima aspa
        elif lt_dados[i] == '"' and flag_aspas:
            flag_aspas = False   
    
    #Criaçao da String
    return ''.join(lt_dados)


file = open('texto.txt','r')   
dados = file.read()       

#Programa principal
print(dados)

#Muda-se o separador dos dados
novo_dados = change(dados,",",";")
print(novo_dados)
    