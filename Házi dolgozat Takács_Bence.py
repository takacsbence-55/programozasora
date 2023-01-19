homersekletek = []
for i in range(30):
    homers = int(input("Adja meg a(z) {}. nap hőmérsékletét: ".format(i+1)))
    homersekletek.append(homers)
average_hom = sum(homersekletek) / len(homersekletek)
print("Az átlaghőmérséklet:", average_hom)

min_hom = min(homersekletek)
print("A legkisebb hőmérséklet:", min_hom)


max_hom = max(homersekletek)
max_hom_index = homersekletek.index(max_hom)
print("A legmelegebb nap hőmérséklete:", max_hom, "és az volt a(z) {}. nap.".format(max_hom_index+1))


fagyottnap = 0
for temp in homersekletek:
    if temp <= 0:
        fagyottnap += 1
print("Ennyi nap fagyott:", fagyottnap)