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

    print(li1)
    print(li2)
        
