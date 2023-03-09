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

for szerzo,cimek in konyvek.items():
    print("Szerző: ",szerzo)
    for cim,adatok in cimek.items():
        print("\t könyv: ",cim,)
        for Adat_kulcs,Adat_érték in adatok.items():
            print("\t\t",Adat_kulcs,Adat_érték)

#for i in konyvek.keys():
    #print(i," : ",konyvek[i])