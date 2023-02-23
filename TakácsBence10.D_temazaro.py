def rendezes(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

    return lista

lista = []
while True:
    a = int(input("Adj meg EGÉSZ számokat: "))
    if a != 0:
        lista.append(a)

    else:
        break

print("Eredeti lista", lista)
lista2 = rendezes(lista)
print("Rendezett lista", lista2)