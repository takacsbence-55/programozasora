import copy

def teljes_hossz(zenek):
    osszeg = 0
    for i in zenek:
        osszeg = osszeg + i["hossz"]

    perc = int(osszeg/60)
    mp = int(60*(osszeg/60-perc))
    with open("02_hossz.txt","w", encoding="utf-8") as file:
        file.write("A lejátszási lista hossza: "+str(perc)+"perc"+str(mp)+"másodperc")

def leggyakoribb_mufaj(zenek):
    mufajok = []
    max = 0
    leggyakoribb = ""
    for i in zenek:
        if not i["mufaj"] in mufajok:
            mufajok.append(i["mufaj"])

    for i in mufajok:
        db = 0
        for j in zenek:
            if j["mufaj"] == i:
                db = db + 1
        if db > max:
            max = db
            leggyakoribb = i

    with open("04_kedvenc_mufaj.txt","w", encoding="utf-8") as file:
        file.write(leggyakoribb.upper())

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
teljes_hossz(zenek)
leggyakoribb_mufaj(zenek)