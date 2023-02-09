lista = [1,9,-6,11,7,12,120,-96,55,42,300,15,-1]

def novekvo_sorrend(lista):
    for i in range(len(lista)-1):
        for j in (i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

            else:
                if lista[i] > lista[j]:
                    lista[i], lista[j] = lista[j], lista[i]

    return lista

sorrend = novekvo_sorrend(lista)
print(sorrend)