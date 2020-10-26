def selection_sort(vet):
    for i in range(len(vet) - 1):
        p = i
        for j in range(i + 1, len(vet)):
            if vet[j] < vet[i]:
                p = j

                vet[i], vet[p] = vet[p], vet[i]
        #print(vet)

x = [55, 99, 33, 22, 77, 66, 11, 88, 44]
selection_sort(x)
print(x)
 