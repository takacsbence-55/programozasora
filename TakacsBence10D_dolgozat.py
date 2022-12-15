lista = []
maxErtek = -1
minElem = 0

for i in range(5):
    print("Adjon meg egy számot:")
    szam = lista.append(float(input()))

for i in lista:
    if i > maxErtek:
        maxErtek = i

for elem in lista:
    if elem < minElem:
        minElem = elem

print("A legnagyobb elem értéke:",maxErtek)
print("A legkisebb elem értéke:",minElem)