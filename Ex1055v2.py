aux=[]
soma=[]
lista=[]
li1=[]
li2=[]
qtde=int(input())
for i in range(qtde):
    aux=input().split()
    
    aux.sort()
    print(aux)
    p=len(aux)//2
    
    
    for i in range(p):
        li1.append(aux[i])
    for i in range(p, len(aux)):
        li2.append(aux[i])
    print("l1\n" f'{li1}')
    print("l2\n" f"{li2}")
    c=0
    for i in range(len(li1)-1,-1,-1):
        lista.append(int(li1[i]))
        lista.append(int(li2[i]))

    print(lista)
    s=0
    for i in range(len(lista)-1):
        s=s+(abs(lista[i]-lista[i+1]))
    
    soma.append(s)
    print(soma)
        

   
        
