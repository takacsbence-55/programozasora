t = [3,8,2,4,5,1,6]

n = len(t)
ker = 5

i = 0
while t[i] != ker:
    i = i + 1

print("Hányadik helyen van:",i+1)

#kiválogatás
a = [3,8,2,4,5,1,6]
b = []

for elem in a:
    if elem < 5:
        b.append(elem)

print(b)