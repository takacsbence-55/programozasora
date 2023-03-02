konyvek = {}
while True:
    cimek = []
    szerzo = input()

    if szerzo == "":
        break
    else:
        while True:
            cim = input()
            if cim == "":
                break
            else:
                cimek.append(cim)
        konyvek[szerzo] = cimek

for i,j in konyvek.items():
    print(i," : ",j)

#for i in konyvek.keys():
    #print(i," : ",konyvek[i])