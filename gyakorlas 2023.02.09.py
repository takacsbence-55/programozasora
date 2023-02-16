def harommal_oszthato(lista):
    db = 0
    for i in lista:
        if i%3==0:
            db = db+1

    return db

def is_negative(szam):
    if szam < 0:
        return True
    else:
        return False

egyedi_lista = []
while True:
    megadott_szam = int(input("Adj meg számokat: "))
    if is_negative(megadott_szam):
        break
    else:
        egyedi_lista.append(megadott_szam)


db = harommal_oszthato(egyedi_lista)
print(db)