# Lê a quantidade de testes
q = int(input())
# Inicia a lista com a qtde de swap de cada trem, para imprimi-la somente no final e inicia os loops para receber os trens

for j in range(q):
    # Acumulador da quantidade de trocas
    trocas = 0
# Recebe a qtde de vagões e os vagões, dividindo os vagões em uma lista e adicionando apenas a qtde informada na lista
    n=int(input())
    q=input().split()
    trem=[]
    for i in range(n):
        trem.append(int(q[i]))
    # Variar 4 até 1
    for nVag in range(len(trem), 0, -1):
        #print(nVag)
        for posVag in trem:
            if nVag == posVag:
                pos = trem.index(nVag)
                #print(pos)
                if pos == (len(trem)-1):
                    pass
                elif trem[pos] > trem[pos+1]:
                    trem[pos], trem[pos+1] = trem[pos+1], trem[pos]
                    trocas += 1                  
    print('Optimal train swapping takes',trocas,'swaps.')
  