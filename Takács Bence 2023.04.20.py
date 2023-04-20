import copy

zenek = []
szotar = {}

with open("playlist.csv","r", encoding="utf-8") as file:
    for sor in file:
        szotar["eloado"] = sor.strip().split(";")[0]
        szotar["cim"] = sor.strip().split(";")[1]
        szotar["mufaj"] = sor.strip().split(";")[2]
        szotar["hossz"] = int(sor.strip().split(";")[3])
        zenek.append(copy.deepcopy(szotar))

print(zenek)