# URI Online Judge | 1162 - Organizador de Vagões
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1162

#recebe a quantidade de trens 
q=int(input())

#inicia a lista com a qtde de Swamps de cada trem, para imprimi-la somente no final e inicia os loops para receber os trens
resul=[]
for j in range(q):

#recebe a qtde de vagões e os vagões, dividindo os vagões em uma lista e adicionando apenas a qtde informada na lista
    swamp=0
    correto=0
    n=int(input())
    q=input().split()
    vagoes=[]
    for i in range(n):
        vagoes.append(q[i])

#inicia o ciclo para verificar se todos os numeros estão corretos
    while correto<len(vagoes):

#loop para comparar os e coloca-los na ponte (variavel aux)
        for i in range(len(vagoes)-1):
            
            aux=[]

            
            aux.append(vagoes[i])
            aux.append(vagoes[i+1])
#verifica se os vagões na ponte estão em ordem e senão, organiza os dois e atualiza a lista vagões com as suas posições corretas           
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
#enquanto a variavel 'correto' não for igual ao tamanho da lista 'vagões' o ciclo será executado e a variavel 'swamp' será incrementada em +1
    resul.append(swamp)

#imprimi todos os 'swamps' obtidos separadamente
for r in resul:
    print('Optimal train swapping takes',r,'swaps.')

   