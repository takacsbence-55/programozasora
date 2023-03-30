def csokkeno(lista):
    for i in range(0,len(lista)-1):
        for j in range(i,len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

lista = []
with open("egysoros.txt","r",encoding="utf-8") as file:
    for sor in file:
        lista = sor.strip().split(";")

for i in range(len(lista)):
    lista[i] = int(lista[i])

csokkeno(lista)
print("EGYSOROS")#egysoros vegerol kitorolve a felesleg
print(lista)

lista2 = []
with open("többsoros.txt","r",encoding="utf-8") as file:
    lista2.append(sor.strip().split(";"))

for i in range(len(lista2)):
    for j in range(len(lista2[i])):
        lista2[i][j] = int(lista2[i][j])

print("TÖBBSOROS")
for i in range(len(lista2)):
    



egy = ""
for i in lista:
    egy = egy+str(i)+";"


with open("egysoros_eredmény.txt","w") as file:
    file.write(egy)

with open("többsoros_eredmény.txt","w") as file:
    for i in lista2:
        sor = ""
        for j in i:
            sor = sor+str(j)+";"
        file.write(sor+"\n")