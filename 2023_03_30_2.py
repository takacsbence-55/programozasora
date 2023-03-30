print("Első feladat")

for i in range(1):
    a = int(input("Adj meg egy számot: "))
    b = int(input("Adj meg még egy számot: "))
    if a > b:
        print("Ez a szám a nagyobb:", a)
    elif b > a:
        print("Ez a szám a nagyobb:", b)
    elif a == b:
        print("A két szám egyenlő.")

print("Második feladat")
def kodolas(mondat,betu,darab):
    cserel = ""
    db = 0
    for i in mondat:
        if i == betu and db < darab:
            cserel = cserel+str(ord(i))
            db = db+1
        else:
            cserel = cserel + i
    return cserel

szoveg = kodolas("Valami szöveget kell megadni","a",2)
#szoveg = kodolas(input("Adj meg egy mondatot: "),str(input("Add meg melyik betűt szeretnéd átalakítani: ")),int(input("Add meg hány betűt szeretnél átalakítani: ")))
print(szoveg)