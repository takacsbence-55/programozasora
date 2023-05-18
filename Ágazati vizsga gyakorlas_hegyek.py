import copy

hegyek = []
dict = {}
with open("hegyekMo.txt","r",encoding="utf-8") as file:
    i = 0
    for sor in file:
        if i != 0:
            dict["Hegycsúcs neve"] = sor.strip().split(";")[0]
            dict["Hegység"] = sor.strip().split(";")[1]
            dict["Magasság"] = int(sor.strip().split(";")[2])
            hegyek.append(copy.deepcopy(dict))

        else:
            i = i+1

minimum = hegyek[0]["Magasság"]
hegy = hegyek[0]["Hegycsúcs neve"]
atl = 0
borzsony = []
for i in hegyek:
    atl = i["Magasság"]+atl
    if i["Magasság"] < minimum:
        minimum = i["Magasság"]
        hegy = i["Hegycsúcs neve"]


    if i["Hegység"] == "Börzsöny":
        borzsony.append(i)

print("B feladat")
print(str(minimum)+" "+hegy)

atl = round(atl/len(hegyek),2)
print("C feladat")
print(atl)

with open("borzsony.txt","w",encoding="utf-8") as file:
    for i in borzsony:
        file.write(i["Hegycsúcs neve"]+" "+str(i["Magasság"])+"\n")