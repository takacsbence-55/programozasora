def csokkeno(lista):
    for i in range(0,len(lista)-1):
        for j in range(i,len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

lista = []

with open("egysoros.txt","r",encoding="utf-8") as file:
    for sor in file:
        lista = sor.split(";")

csokkeno(lista)
print(lista)