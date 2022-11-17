lista_magassagok = []

osztaly_letszam = 3
magassag = 0
for i in range(osztaly_letszam):
    magassag = float(input())
    lista_magassagok.append(magassag)

legnagyobb = 0

for i in lista_magassagok:
    if i > legnagyobb:
        legnagyobb = i

print(legnagyobb)