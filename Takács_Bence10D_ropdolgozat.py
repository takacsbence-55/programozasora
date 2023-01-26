lista = [10,-2,1,25,22,30,60,-99,-1252,3000,2123,16,12]

for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        print(lista)
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
            print("csere")
        else:
            print('')

print(lista)

print("csökkenő sorrend")
for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        print(lista)
        if lista[i] < lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
            print("csere")
        else:
            print('')