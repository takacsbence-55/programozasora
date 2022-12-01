t = [3,8,2,4,5,1,6]

osszeg = 0
for num in t:
    osszeg = osszeg + num

print("Összeg:",osszeg)


t = [5,3,6,2,1]

minElem = t[0]
for elem in t:
    if elem < minElem:
        minElem = elem

print(minElem)


t = [5,3,6,2,1]

minElem = t[0]
for i in range(1,len(t)):
    if t[i] < minElem:
        minElem = t[i]
        minhely = i

print(minElem,minhely)


t = [3,-8,2,4,5,11,6]

count = 0
for num in t:
    if num < 0:
        count = count + 1

print("negatív számok:",count)


