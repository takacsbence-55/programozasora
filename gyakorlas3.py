lista1 = [-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-7,5,80,-77,100,67,22,8,-78,-6]

darabszam = len(lista1)

print(darabszam)
print("1. :",darabszam)

#van-e negatív szám?
i = 0

while i<darabszam and lista1 [i] >= 0:
    i = i+1

if i < darabszam:
    print("2. : Van")
else:
    print("2. : Nincs")


#hány páros szám van a listában?
count = 0

for i in lista1:
    if i % 2 == 0:
        count = count+1
print("3. :",count)


#mennyi a listában található legnagyobb szám?
maxErtek = lista1[0]
for i in lista1:
    if i > maxErtek:
        maxErtek = i
print("4. :",maxErtek)


#10-el osztható számok
print("5.feladat")
for i in lista1:
    if i % 10 == 0:
        print(i)


#6. az első 29-el osztható szám indexe
i = 0
while i < darabszam and lista1[i] %29 != 0:
    i = i+1
print("6. :",i,"érték",lista1[i])


#7. igaz-e hogy minden szám páros?
logikai = True

i = 0

while i < darabszam and lista1[i] % 2 == 0:
    i = i+1
if i < darabszam:
    logikai = False
print("7. :",logikai)


#8. mennyi a listában található számok átlaga?
atlag = 0
osszeg = 0

for i in lista1:
    osszeg = round(osszeg +i,2)

atlag = osszeg/darabszam
print("8. :",atlag)