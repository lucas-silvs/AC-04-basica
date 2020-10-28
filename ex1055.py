def addperm(x,l):
    return [ l[0:i] + [x] + l[i:]  for i in range(len(l)+1) ]

def perm(l):
    if len(l) == 0:
        return [[]]
    return [x for y in perm(l[1:]) for x in addperm(l[0],y) ]
soma=[]
qtde=int(input())
for i in range(qtde):
    aux=input().split()
    
    lista=perm(aux)
    som=0
    for i in range(23):
        s=0
        
        print(lista[i])
        for n in range(len(lista[i])-1):
            s=s+(abs(int(lista[i][n])-int(lista[i][n+1])))
        print(s)
        if (som<s):
            som=s
    soma.append(som)
        

print(soma)
