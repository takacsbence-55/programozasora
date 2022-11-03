lista = [1,2,3,4,5,6,7]
lista[0] = 100
print(lista[0])

for i,j in enumerate(lista):
    print(i,j)
    lista[i] = lista[i]+100
    print(i,lista[i])


#program ami bekér 5 számot, ezt eltárolja egy listába és a végén kiírja a listát, az átlagot és a legnagyobb értéket,
#az indexel együtt
#lista.append(amit a listába akarsz adni)

lista = []
osszeg = 0
maximum = -1
for i in range(5):
    a = int(input())
    lista.append(a)
    osszeg = osszeg+a
    if maximum < a:
        maximum = a

print(lista)
print(osszeg/len(lista))
print(maximum,lista.index(maximum))

#lista minden eleméhez hozzáadjuk a maximumot és elosztjuk az átlaggal