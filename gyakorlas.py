#homersekletszamitas
# F to C = (F-32)/1.8
# C to F = C*1.8+32

homerseklet = float(input("Add meg az alap hőfokot:  "))
print("Add meg a mértékegységet. C = Celsius, F = Fahrenheit, K = Kelvin.")
mertekegyseg = input()

if mertekegyseg == "C":
    #Alap hőmérséklet celsius egységben van
    #celsiust nem kell számolni
    #F-et kell számolnom C to F = C*1.8+32
    #Ezt külön változóba teszem
    #kiiratom az összes egységet
    F = homerseklet*1.8*32
    K = homerseklet+273.15
    print("A hőmérséklet celsiusban: ", homerseklet, "Celsius")
    print("A hőmérséklet fahrenheitben: ", F, "Fahrenheit")
    print("A hőmérséklet kelvinben: ", K, "Kelvin")

elif mertekegyseg == "F":
    C = (homerseklet-32)/1.8
    K = C+273.15
    print("A hőmérséklet celsiusban: ", C, "Celsius")
    print("A hőmérséklet fahrenheitben: ", homerseklet, "Fahrenheit")
    print("A hőmérséklet kelvinben: ", K, "Kelvin")

elif mertekegyseg == "K":
    C = homerseklet-273.15
    F = C*1.8+32
    print("A hőmérséklet celsiusban: ", F, "Celsius")
    print("A hőmérséklet fahrenheitben: ", C, "Fahrenheit")
    print("A hőmérséklet kelvinben: ", homerseklet, "Kelvin")