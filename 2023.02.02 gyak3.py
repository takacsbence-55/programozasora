def minimum(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min

lista = []
while True:
    a = int(input("Add meg a számot: "))
    if a != 0:
        lista.append(a)
    else:
        break

min = minimum(lista)
print("A legkisebb szám:",min)