# URI Online Judge | 1260
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1260

while True:
    q = input()
    if q == '':
        break
    input()
    qtde = int(q)
    f=[]
    # pede a quantidade de testes   
    aux=1
    for i in range(qtde):
        
    #enquanto a entrada for diferente de ' ', pede entrada.
        
        lArv=[]
        final=[]
        
        while True:
            arv = input()
            if arv == '':
                break
            else:
                lArv.append(arv)
            
        
        
        

        valor=[]
        calc=100/len(lArv)
        #transf lArv em set
        ordLarv = set(lArv)
        ordLarv = list(ordLarv)
        ordLarv.sort()
        

        for j in ordLarv:
            final.append(j+" {:6.4f}".format(lArv.count(j) * calc))
       
        
        f.append(final)

        
        
        
       
            
        
        
   
    aux=0
    for l in f:
        for arvo in l:
           print(arvo)
        aux+=1
        if(aux<qtde):
            print()


    
        
    
  
    break
    
            

