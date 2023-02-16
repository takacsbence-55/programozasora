def novekvosorrend(lista):
    for i in range(len(lista)-1):
        for j in (i+1,len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

    return lista

def minErtek(lista):
    minimum = lista[0]
    for i in lista:
        if i < minimum:
            minimum = i

    return minimum

def maxErtek(lista):
    maximum = lista[0]
    for i in lista:
        if i > maximum:
            maximum = i

    return maximum


lista = [1,9,-6,11,7,12,120,-96,55,42,300,15,-1]
lista = novekvosorrend(lista)
print(lista)
print(minErtek(lista))
print(maxErtek(lista))