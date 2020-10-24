# URI Online Judge | 1162 - Organizador de Vagões
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1162

#recebe a quantidade de trens 
q=int(input())

#inicia a lista com a qtde de Swamps de cada trem, para imprimi-la somente no final e inicia os loops para receber os trens
resul=[]
for j in range(q):

#recebe a qtde de vagões e os vagões, dividindo os vagões em uma lista e adicionando apenas a qtde informada na lista
    swamp=0
    n=int(input())
    q=input().split()
    vagoes=[]
    for i in range(n):
        vagoes.append(int(q[i]))

#segundo loop para verificar se as posições correspondem com o numero do vagão
    for i in range(len(vagoes)):
        t=1
        s=0
        print("indice",i)
        #enquanto os vagões não forem ordenados igual suas posições, o swamp é executado
        while vagoes[i] != i+1:  
            s=0  
            vagoes[i], vagoes[i+t] = vagoes[i+t], vagoes[i]
            s += t 
            t=t+1 
            print(vagoes)
        #o Swamp só é adicionado na variavel quando é obteve o número correto 
        swamp+=s 
        print("swamp add:",swamp)
        
        s=0

# adiciona lista de resultados a lista de resultados
    resul.append(swamp)
#imprimi todos os 'swamps' obtidos separadamente
for r in resul:
    print('Optimal train swapping takes',r,'swaps.')  


#swamp=len(vagoes)-(i+1)