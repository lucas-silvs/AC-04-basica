# URI Online Judge | 1162 - Organizador de Vagões
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1162

while True:
    
    q=int(input())
    
    for j in range(q):
        swamp=0
        correto=0
        n=int(input())
        vagoes=input().split()


        while correto<len(vagoes):
            for i in range(len(vagoes)-1):
                
                aux=[]
                
                aux.append(vagoes[i])
                aux.append(vagoes[i+1])
                
                if(aux[0]>aux[1]):
                    a=aux[0]
                    aux[0]=aux[1]
                    aux[1]=a
                    vagoes[i]=aux[0]
                    vagoes[i+1]=aux[1]
                    swamp+=1
            

            for i in range(len(vagoes)-1):
                if(vagoes[i]<vagoes[i+1]):
                    correto+=1

        print(f'Optimal train swapping takes {swamp} swaps.')

    break