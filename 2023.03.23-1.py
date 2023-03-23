def rendez(lista):
    for i in range(0,len(lista)-1):
        for j in range(i,len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

felsorolas = []
with open("lista.txt","r", encoding="utf-8") as file:
    for sor in file:
        felsorolas = sor.split(";")

for i in range(len(felsorolas)):
    #print(felsorolas[i])
    felsorolas[i] = int(felsorolas[i])

rendez(felsorolas)
print(felsorolas)
print("Legkisebb szám:",felsorolas[0])
print("Legnagyobb szám:",felsorolas[len(felsorolas)-1])


rendez(felsorolas)
st = ""
for i in felsorolas:
    st = st+str(i)+" "

with open("ujlista.txt","w",encoding="utf-8") as file:
    file.write(st+"\n")
    file.write("Minimum: "+str(felsorolas[0])+"\n")
    file.write("Maximum: "+str(felsorolas[len(felsorolas)-1]))