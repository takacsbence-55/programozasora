napok = [-5,10,20,30,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,33]

sum = 0

#for i in range(30):
  #  a = float(input())
 #   napok.append(a)
#    sum = sum+a
min = napok[0]
max = napok[0]
max_index = 0
count = 0
for n,i in enumerate(napok):
    sum = sum+i
    if i < min:
        min = i
    if i > max:
        max = i
        max_index = n
    if i < 0:
        count = count+1

atl = sum/len(napok)

print("Az átlag hőmérséklet:",atl, "C fok")
print("A legkisebb hőmérséklet:",min, "C fok")
print("A legnagyobb hőmérséklet:",max, "ami a",max_index, "napon történt")
print(count,"alkalommal fagyott")