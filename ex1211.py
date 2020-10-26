#URI 1211- Lista telefonica Economica
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1211


#inicia o looping até que o usuario digite 0 nas quantidades de numeros
while True:
    try:
        f=0
        x=int(input())
       

        #inicia a lista de numeros "num" e começa o loop para adição dos 
        # números a lista

        num=[]
        for i  in range (x):
            num.append(input())
            num.sort()


        #inicia a verificação se os numeros são iguais e se o primeiro é igual
        
        for i in range(len(num)-1):
            q=0
            for j in range (len(num[i])):
                if(num[i][j]==num[i+1][j]):
                    q+=1
                else:
                    break
            if(f<=q):
                f=q

        #printa o resultado das repetições
        print(f)
    except EOFError:
        break

