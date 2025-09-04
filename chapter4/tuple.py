"""
✅ 1. What is a Tuple?

Tuple ek collection data type hai (jaise list hoti hai).
Ordered hota hai → elements same order me rahte hain.
Immutable hota hai → ek baar ban gaya to uske elements change nahi kar sakte.
Duplicates allow karta hai.
Tuple ko round brackets () me likha jata hai.
"""

# empty tuple
a=()
# tuple with one element:, is necessary for one elemnts
a=(1,)
# tuple with more than neelements
a=(1,5,5)


# A tuple is a immutable datatype in python
a=(1,2,3)
print(type(a))   #class tuple
a=()
print(type(a))     #class tuple

'''
a=(1,"sagar",False)
a[0]=25
print(a)     #tpe error q ki ye immutable hai change nhi kar sakte h hm 
'''


# tuple ke basically 2 methods hote hai
t=(1,2,3,2,4)
print(t.count(2))    #output:2
print(t.index(4))     #output:4

# extra function that work with tuples
t=(10,20,30,40,650)
print(len(t))       #output:5

t=(2,3,5)
print(sum(t))    #output:10


t=(10,6,5)
print(min(t))

t=(4,2,3,5)
print(sorted(t))   #[2,3,4,5]

t=(0,0,5)
print(any(t))    #true

t=(1,2,3)
print((all(t)))    #true

t=(1,0,3)
print((all(t)))    #False

t=[10,20,30]
print(tuple(t))     #tuple method kisi v string ya list ko tuple me convert kar deta h

t1="abc"
print(tuple(t1))     #('a', 'b', 'c')


# operation with tuples
# 1. concatination
t1=(1,2)
t2=(3,4)
result=t1+t2
print(result)
# 2. Repetition
t=(1,2)
print(t*2)    #output:(1, 2, 1, 2)

# membership test
t=(10,20,30)
print(20 in t)    #output:True

# indexing
t=('a',"b","c")
print(t[0])    #output:a

# slicing
t=(0,1,2,3,4,5)
print(t[1:4])    #output:(1,2,3)

# unpacking:assign tupple elements to variable
t=(1,2,3)
a,b,c=t
print(a,b,c)   #output:123

# looping through a loop
fruits=('apple','banana','cherry')
for fruit in fruits:
    print(fruit)
    '''
    output:
    apple
    banana
    cherry
    '''



# nested tuples
t=(1,(2,3),4)
print(t[1])     #output:(2,3)
print(t[1][0])     #output:(2)

# tuple comparision
'''
tuples are compared elements by elements
'''

print((1,2)<(1,3))      #Output:True
print((2,0)>(1,5))      #Output:True
print((1,2)<(1,3))      #output:true 

# ek hi check krenge bata denge agar phle false aa jaaye to false hi aayega agar phle true aa jaayega to true hi aayega same same aayega to next wala se compare krenge
print((1,2)<(1,2,0))    #output: True  left wale 2 ke right me kuch nhi hai to end bolenge usko (shorter<longer)









