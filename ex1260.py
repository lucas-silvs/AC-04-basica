# URI Online Judge | 1260
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1260

#inicia o loop pedingo a qtde de casos
while True:
    q = input()
    if q == '':
        break
    input()
    qtde = int(q)
    f=[]
    
    aux=1

    #segundo loop que será a entrada das arvores
    for i in range(qtde):
        
    
        
        lArv=[]
        final=[]
        #enquanto a caixa de texto não for enviada vazia, será add na lista
        while True:
            arv = input()
            if arv == '':
                lArv.append(arv)
                False
            else:
                lArv.append(arv)
            
        
        
        
        #calcula o valor de uma ocasião baseado no tamanho da lista
        valor=[]
        calc=100/len(lArv)
        #transf lArv em set
        ordLarv = set(lArv)
        ordLarv = list(ordLarv)
        ordLarv.sort()
        
        #add em outra lista o nome da arvore e a qtde de ocorrencia * o valor de uma ocasião
        for j in ordLarv:
            final.append(j+" {:6.4f}".format(lArv.count(j) * calc))
       
        #add a lista com todos os valores em outra lista para a impressão
        f.append(final)

        
        
        
       
            
        
        

    aux=0
    for l in f:
        aux+=1
        
        for arvo in l:
           print(arvo)
        if(aux<qtde):
            print()
        


    
        
    
  
    break
    
            

