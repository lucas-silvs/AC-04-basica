# URI Online Judge | 1259

lista_impar = []
lista_par = []


# repete quantas vezes entrar em quantidade
qtde = int(input())
for i in range(qtde):
    n = int(input())
    if n % 2 == 0 and n>0:
        lista_par.append(n)
    elif  n % 2 != 0 and n>0:
        lista_impar.append(n)
    
lista_impar.sort(reverse=True)
lista_par.sort()
f = lista_par + lista_impar

print(f)
