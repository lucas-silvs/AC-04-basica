#Atividade URI 1251 - Diga-me a Frequência
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1251


while True:
    try:
        

        #Inicia e da entrada na lista, depois gera um set auxiliar para remover 
        # os repetidos
        d=[]
        d=list(input())
        daux=list(set(d))
        daux.sort()
        #inicia a lista de contagem 
        c=[]
        #loop para contar as ocorrencias e colocar na como uma lista a letra 
        # em ASCII e a qtde de ocorrencias 
        for i in daux:
            
            c.append([str(ord(i)),str(d.count(i))])


        #ordenar a partir da quantidade de ocorrencias

        c.sort(key= lambda k:k[1])


        #printar na tela :)
        for i in c:
            print("%s %s"%(i[0],i[1]))
        print()
    except EOFError:
        break

