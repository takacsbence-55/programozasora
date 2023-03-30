import copy

def rendez(lista):
    for i in range(0,len(lista)-1):
        for j in range(i,len(lista)):
            if lista[i][1] > lista[j][1]:
                lista[i], lista[j] = lista[j], lista[i]

EU = []
EU2 = []
dic = {}
with open("EU.txt","r",encoding="utf-8") as file:
    for sor in file:
        dic["Ország név"] = sor.strip().split(" ")[0]
        dic["Belépési év"] = int(sor.strip().split(" ")[1])
        EU2.append(copy.deepcopy(dic))
        EU.append(sor.strip().split(" "))

for i in range(len(EU)):
    EU[i][1]= int(EU[i][1])

min = EU[0][1]
for i in EU:
    if i[1] < min:
        min = i[1]

dbe = 0
dbb = 0
db6  =0
legrövh = len(EU[0][0])
legrövn = EU[0][0]
for i in EU:
    if i[0][0] == "B":
        dbb = dbb+1
    if len(i[0]) > 6:
        db6 = db6+1
    if len(i[0]) < legrövh:
        legrövh = len(i[0])
        legrövn = i[0]
    if i[1] == min:
        dbe = dbe+1

print("Első csatlakozó szám:", dbe)
print("B betűvel kezdődő:", dbb)
print("6-nál hosszabb:", db6)
print("Legrövidebb hossz:", legrövh)
print("Legrövidebb név:", legrövn)
print(EU2)