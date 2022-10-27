homerseklet = float(input("Add meg az alap hőfokot:  "))
print("Add meg a mértékegységet. C = Celsius, F = Fahrenheit, K = Kelvin.")
mertekegyseg = input()
mibe = input()

if mertekegyseg == "C":
    if mibe == "C":
        print("A", homerseklet,"Celsius fok az ",homerseklet,"Celsius fok")