#x = list("alma")
#print(x)

#1. feladat

szovegem = input()
db = 0
szamok = "0123456789"
for i in szovegem:
    if i in szamok:
        db = db +1
        print(i)

print("Számok a szövegben:", db,"db")