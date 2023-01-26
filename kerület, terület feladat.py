def ter(a,b):
    t = a*b
    return t
def ker(a,b):
    k = 2*(a+b)
    return k

aoldalak = [10,5,2,4]
boldalak = [8,6,7,9]
teruletek = []
keruletek = []
for i,j in zip(aoldalak,boldalak):
    teruletek.append(ter(i,j))
    keruletek.append(ker(i,j))

print(keruletek)
print(teruletek)