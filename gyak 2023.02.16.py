#stringek

a = "abcde"

for i in a:
    print(i,end=" ")

print()

for j in range(0,len(a),2):
    print(a[j], end=" ")

print()
#(másik megoldás)
#for k in a:
    #print(ord(k), end=" ")
for k in range(0,len(a),1):
    print(ord(a[k]), end=" ")