konyvek = {}
while True:
    cimek = {}
    szerzo = input("Adj meg egy szerzőt: ")

    if szerzo == "":
        break
    else:
        while True:
            cim = input("Adj meg egy címet: ")
            if cim == "":
                break
            else:
                kiadas = int(input("Add meg a kiadási évet: "))
                kategoria = input("Add meg a kategóriát: ")
                leiras = input("Add meg a tartalmát: ")
                cimek[cim] = {"Kiadási év":kiadas,"kategória":kategoria,"Tartalom":leiras}
        konyvek[szerzo] = cimek

for i,j in konyvek.items():
    print(i," : ",j)

#for i in konyvek.keys():
    #print(i," : ",konyvek[i])