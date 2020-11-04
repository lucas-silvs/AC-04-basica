soma=[]
qtde=int(input())

for i in range(qtde):
    aux=[]
    lista=[]
    ln=0
    l=input().split()

    aux=[int(i)for i in l]
    ln=int(l[0])
    del(aux[0])
    aux.sort()
    p=len(aux)//2
    c=True
    if(len(aux) %2==0):
        
        while aux!=[]:
            if(c==True):
                lista.insert(0,aux[len(aux)-1])
                lista.append(aux[0])
                del(aux[0])
                del(aux[len(aux)-1])
                c=False
            else:
                lista.insert(0,aux[0])
                lista.append(aux[len(aux)-1])
                del(aux[0])
                del(aux[len(aux)-1])
                c=True
    
    else:
         while aux!=[]:
            if(len(aux)==1):
                if(abs(aux[0]-lista[0])>=abs(lista[len(lista)-1]-aux[0])):
                    lista.insert(0,aux[0])
                else:
                    lista.insert(len(lista)-1,aux[0])
                break
            if(c==True):
                lista.insert(0,aux[len(aux)-1])
                lista.append(aux[0])
                del(aux[0])
                del(aux[len(aux)-1])
                c=False
            else:
                lista.insert(0,aux[0])
                lista.append(aux[len(aux)-1])
                del(aux[0])
                del(aux[len(aux)-1])
                c=True
    somanumero=0
    for i in range(len(lista)-1):
        somanumero=somanumero+abs(lista[i]-lista[i+1])
    print(f'Case {i+1}: {somanumero}')