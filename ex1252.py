# URI Online Judge | 1252 - Sort! Sort!! e Sort!!!
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1252



while True:
    n,d=input().split()
    n=int(n)
    d=int(d)
    if( n==0 and d==0):
        break
    numeros=[]
    for i in range(n):
        numeros.append(int(input()))
    
    mod=[]
    for i in numeros:
        mod.append([i,i%d])
    pares=[]
    impares=[]
    for i in mod:
        if(i[0]%2==0):
            pares.append(i)
        else:
            impares.append(i)
        pares.sort(key=lambda x:x[0])
        pares.sort(key=lambda x:x[1])
        impares.sort(key=lambda x:x[0], reverse= True)
        impares.sort(key=lambda x:x[1])
    indice=-1
    final=[]
    imp=0

    print(pares)
    print()
    print(impares)
    print()
   
    while(impares!=[] and pares!=[]):
        
        indice+=1
        if(impares==[]):
                break
        else:
            while impares[0][1]==indice:
                    final.append(impares[0][0])
                    del(impares[0])
                
        print(final)
        print("Impares:",impares)
        
        if(pares==[]):
            break
        else:   
            while pares[0][1]==indice:
                    final.append(pares[0][0])
                    del(pares[0])
        
        print(final)
        print("Pares:",pares)
        
        
    print(final)
