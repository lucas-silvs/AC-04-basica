# URI Online Judge | 1258
final=[]
ocorrencia=0
while True:

    
    # Pede quantidade de camisetas enquanto != 0
    n = int(input())
    # Cria vetor(nome, cor e tamanho)
    qtCam = [[0,0,0] for i in range(n)]

    # Pede nome, tamanho e cor e atribui no vetor
    for i in range(len(qtCam)):
        #pede o nome
        nome = input()
        #pede cor e tamanho e separa
        corTam = input().split()
        cor = corTam[0]
        tam = corTam[1]
        #preenche no vetor
        qtCam[i][0] = nome
        qtCam[i][1] = cor
        qtCam[i][2] = tam
        # qtCam = [[nome, cor, tam]]
    qtCam.sort(key=lambda x:x[0])
    qtCam.sort(key=lambda x:x[2], reverse=True)
    qtCam.sort(key=lambda x:x[1])
    final.append(qtCam)
#verifica se é a primeira ocorrencia, senão add a linha
    
    if n == 0:
        
        
        for l in final:
            if ocorrencia>0:
                print()
            else:
                ocorrencia+=1
            for a in l:
                print(a[1], a[2], a[0])
           

