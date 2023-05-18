i = int(input("Adj meg egy egész számot: "))

if i % 2 == 0:
    print("A szám páros")
else:
    print("A szám páratlan")

def email(Nev,osztaly):
    Nev = Nev.lower()
    osztaly = osztaly.lower()

    ev = 2023-(int(osztaly.split(".")[0])-8)
    csoport = osztaly.split(".")[1]

    ekezet = ["á","é","í","ő","ű","ú","ó"]
    mentes = ["a","e","i","ö","ü","u","o"]

    for i,j in zip(ekezet,mentes):
        Nev = Nev.replace(i,j)

    Nev = Nev.replace(" ",".")

    Email = Nev+".tech"+str(ev)+csoport+"@bolyaimovar.com"

    return Email

em = email("Takács Bence Miklós","10.D")
print(em)