lista1 = [-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,8,0,-77,100,67,22,8,-78,-6]

for i in range(len(lista1)-1):
    print(lista1)
    minindex = i
    for j in range(i+1,len(lista1)):
        if lista1[j] < lista1[minindex]:
            minindex = j
            print("új minimum találat")
        else:
            print('')
    if i != minindex:
        print("csere")
        lista1[i], lista1[minindex] = lista1[minindex], lista1[i]

print(lista1)