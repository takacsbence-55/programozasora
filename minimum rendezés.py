lista = [7,2,5,3,8,-5,33,6]

for i in range(len(lista)-1):
    print(lista)
    minindex = i
    for j in range(i+1,len(lista)):
        if lista[j] < lista[minindex]:
            minindex = j
            print("új minimum találat")
        else:
            print('')
    if i != minindex:
        print("csere")
        lista[i], lista[minindex] = lista[minindex], lista[i]

print(lista)