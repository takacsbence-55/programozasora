lista1 = [-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,8,0,-77,100,67,22,8,-78,-6]

for i in range(len(lista1)-1):
    for j in range(i+1,len(lista1)):
        print(lista1)
        if lista1[i] > lista1[j]:
            lista1[i], lista1[j] = lista1[j], lista1[i]
            print("csere")
        else:
            print('')
print(lista1)