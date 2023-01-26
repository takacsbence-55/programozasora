lista2 = [7,2,5,3,8,-5,33,6]


def rendez(lista,irany):
    for i in range(len(lista2)-1):
        for j in range(i+1,len(lista2)):
            #print(lista)
            if irany == "Növ":
                if lista2[i] > lista2[j]:
                    lista2[i], lista2[j] = lista2[j], lista2[i]
            else:
               if lista2[i] < lista2[j]:
                    lista2[i], lista2[j] = lista2[j], lista2[i]
                    #print("csere")

rendez(lista2,"Növ")
print(lista2)
rendez(lista2,"Csök")
print(lista2)