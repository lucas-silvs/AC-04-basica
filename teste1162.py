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
        orde=[]
       #  insertion sort que empurra os maiores para o ultimo 
    for i in range(1, len(vagoes)): 
        n = vagoes[i] 
        j = i-1
        while j >= 0 and n < vagoes[j] : 
                vagoes[j + 1] = vagoes[j]
                swamp+=1 
                j -= 1
                print(vagoes)
        vagoes[j + 1] = n

# adiciona lista de resultados a lista de resultados
    print(vagoes)
    resul.append(swamp)
#imprimi todos os 'swamps' obtidos separadamente
for r in resul:
    print('Optimal train swapping takes',r,'swaps.')  



   
