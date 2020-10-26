# URI Online Judge | 1260

while True:
    q = input()
    if q == '':
        break
    print()
    qtde = int(q)
    f=[]
    # pede a quantidade de testes     
    for i in range(qtde):
    #enquanto a entrada for diferente de ' ', pede entrada.
        lArv=[]
        final=[]
        
        while True:
            
            arv = input()
            if arv == '':
                break
            lArv.append(arv)

        valor=[]
        calc=100/len(lArv)
        #transf lArv em set
        ordLarv = set(lArv)
        ordLarv = list(ordLarv)
        ordLarv.sort()
        

        for j in ordLarv:
            final.append(j+" {:6.4f}".format(lArv.count(j) * calc))
        
        for k in final:
            f.append(k)


        for l in f:
            print(l)
        
        if(i<(qtde-1)):
            print()
    
    break
    
            

