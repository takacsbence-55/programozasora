szam = float(input("Adjon meg egy számot: "))
print("Adja meg a mértékegységet(cm, m, km):")
mertekegyseg = input()
print("Adja meg mibe szeretné átváltani:")
mibe = input()

if mertekegyseg == "cm":
    if mibe == "cm":
        print("A",szam,"cm ""az",szam,"cm.")
    elif mibe == "m":
        m = szam/100
        print("A",szam,"cm az",m,"méter.")
    elif mibe == "km":
        km = float(szam/100000)
        print("A",szam,"cm az",km,"kilóméter.")

if mertekegyseg == "m":
    if mibe == "cm":
        cm = szam*100
        print("A",szam,"méter átváltva",cm,"centiméter.")
    elif mibe == "km":
        km = szam/1000
        print("A",szam,"méter az",km,"kilóméter.")

if mertekegyseg == "km":
    if mibe == "cm":
        cm = szam*100000
        print("A",szam,"kilóméter átváltva",cm,"centiméter.")
    elif mibe == "m":
        m = szam*1000
        print("A",szam,"méter az",m,"méter.")