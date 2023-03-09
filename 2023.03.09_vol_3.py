import math


szam = int(input())
if szam > 0:
    prim = True
    j = 2
    gy = math.sqrt(szam)
    while prim and j <= gy:
        if szam % 2 == 0:
            prim = False
        else:
            j = j+1
    if prim:
        print("Prím szám")
    else:
        print("Nem prím szám")
else:
    print("Negatív számot vagy 0-t adtál meg")