a = {1,2,22}
b = {3,4,5}
a.difference_update(b)  #iterable = zaagch
print(a)

# discard funkts bhgui bsan ch aldaa gardaggui funkts
a = {1,2,22}
b = {3,4,5}
a.discard(2)  #iterable = zaagch
print(a)

# intersection
a = {1,2,22,4,5}
b = {3,4,5,33,22}
new = a.intersection(b)  
print(a)

# intersection update
a = {1,2,22,4,5}
b = {3,4,5,33,22}
new = a.intersection_update(b)  
print(a)

#isdisjoint (ogtloltsohgui bgaag true false-oor gargah)
a = {1,2,22,4,5}
b = {3,4,5,33,22}
new = a.isdisjoint(b)  
print(new)

# is subset - ded olonlog oloh arga
a = {1,2,22,4,5}
b = {3,4,5,33,22}
new = a.issubset(b)
print(new)

# is super set - ih olonlog oloh
a = {3,4,5,22} 
b = {1,2,22,4,5}
new = n.issuperset(a)
print(new)

# pop ehnii murund bgaa elementiig avah
a = {3,4}
b = {1,3,4,5,111}
new = b.pop()
print(new)

#2 olonlogiin yalgaatai elementiig avah
a = {3,4,8,9}
b = {1,3,4,5,111}
b.symmetric_difference(a)
print(b)

# olonlogiin negdeliig oloh
a = {3,4,8,9}
b = {1,3,4,5,111}
new = b.union(a)
print(new)

# niilbereer erembleh
a = ["shagai", "tomor", "bold", "od", "baatar", "delger"]
b = [[1,1,1],[1,2][3,4],[-9,-4,0,1]]
a.sort(key=len)
b.sort(key=sum)
print(b)