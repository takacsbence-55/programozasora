#betűsorrend fordítás
#a
a = "valami"
b = ""
for i in range(len(a)-1,-1,-1):
    b = b+a[i]

print(b)

#b
print("A")
a = "sós"
print(a[::-1])
print()
print("B")
if a == a[::-1]:
    print("palindrom")

else:
    print("Nem palindrom")

print()
print("C")
mondat = "Az alma a fán piros"
szó = ""

for i in mondat:
    if i == " ":
        print(szó)
        szó = ""
    else:
        szó = szó+i

print(szó)


for i in mondat.split(" "):
    print(i)