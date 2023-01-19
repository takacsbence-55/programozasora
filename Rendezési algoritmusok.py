lista = [7,2,5,3,8,-5,33,6]

for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        print(lista)
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
            print("csere")
        else:
            print('')

print(lista)