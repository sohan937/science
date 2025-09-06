a={1,2,3}
b={3,4,5}
a.add(6)
a.update([7,8])
print("add and update:",a)    #add and update: {1, 2, 3, 6, 7, 8}

a.remove(2)
print(a)     # {1, 3, 6, 7, 8}

a.discard(10)
print(a)    #no error if item does not exist
a.pop()
print(a)    #random koi v elemts ko delete kr sakta h


copied_set=a.copy()
print("copy of set",copied_set)    #copy of set {8, 3, 6, 7}

union_set=a.union(b)
print("union set:",union_set)      #union set: {3, 4, 5, 6, 7, 8}

intersection_set=a.intersection(b)
print("intersection set:",intersection_set)    # intersection set: {3}

difference_set=a.difference(b)
print("difference set:",difference_set)    # difference set: {8, 6, 7}

x={1,2,3,4}
y={3,4,5,6}
sym_difference=x.symmetric_difference(y)
print(sym_difference)      #{1, 2, 5, 6}    jo common hoga wo nhi likhenge


s={1,2}
t={1,2,3,4}
print(s.issubset(t))     #True

s={1,2,3,4}
t={1,2}
print(s.issuperset(t))     #True

A = {1, 2, 3}
B = {4, 5, 6}
print(A.isdisjoint(B))   # True   dono menkoi common elements nhi ho

fruits={"apple","banana"}

# print(fruits.clear())    #None
fruits.clear()
print(fruits)      #output:set()








