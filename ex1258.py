# EX URI 1258 - Camisetas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1258



while True:

    q=int(input())
    if q==0:
        break


    camisas=[]
    for i in range(q):
        nome=""
        cortamanho=""
        nome=input()
        cortamanho=input().split()
        camisas.append([nome,cortamanho[0], cortamanho[1]])

    
    print(camisas)
