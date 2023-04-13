autok = []

with open("autok.csv","r", encoding="utf-8") as file:
    for sor in file:
        autok.append(sor.strip().split(";"))

print(autok)

autok = autok[1:]
for i in range(len(autok)):
    autok[i][4] = int(autok[i][4])

indulas = "Munkács"
cel = "Záhony"
ferohely = 0
db = 0
budapest = []

for i in autok:
    if i[0] == indulas and i[1] == cel:
        ferohely = ferohely+i[4]

    db = db+i[4]

    if i[0] == "Budapest":
        budapest.append(i[1]+" "+i[3])

atl = round(db/len(autok),1)

print("b feladat",ferohely,"\n")
print("c feladat",atl,"\n")
print("d feladat",budapest)

with open("budapest.dat","w", encoding="utf-8") as file:
    for i in budapest:
        file.write(i+"\n")