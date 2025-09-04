# list:lists are container to store a set of values of any data types.lists are immutable.
# simple si baat list me different types of data types ko store kar sakte hai


"""
🔹 What is a List in Python?

A list is a collection of items in Python.

It can store different data types (integers, strings, floats, even other lists).

Lists are ordered, mutable (changeable), and allow duplicate values.

Lists are written with square brackets [ ].

"""
data=["apple","akash",7,False,37.2]

l1=[3,5,"sagar"]
print(l1[0])   #output:3

print(l1[0:2])   #output:[3,5]

                         # In REPL example
"""
windows pe right click open terminal
>>>
KeyboardInterrupt
>>> a="sagar"
>>> a[0]
's'
>>> a[5]
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    a[5]
    ~^^^
IndexError: string index out of range
>>> a[3]="a"
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    a[3]="a"
    ~^^^
TypeError: 'str' object does not support item assignment
>>>
"""
            #   properties

# ordered example
a = [1, 2, 3]
print(a[0])   # 1

# mutable example
a = [1, 2, 3]
a[1] = 100
print(a)   # [1, 100, 3]

# duplicate example:ek hi value list me baar baar ho sakti hai
numbers = [10, 20, 10, 30, 20, 40]
print(numbers)

# different data types
a = [10, "Python", 3.14]
print(a)   # [10, 'Python', 3.14]




                                         # accessing elements
a = [10, 20, 30, 40]
print(a[0])   # 10
print(a[-1])  # 40 (negative index means from end)

                                                    # looping in a list

fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)       
    '''
    output:
    apple
    banana
    cherry
    '''
                                                 
# lists operation
'''
 Adding Elements

append() → end me add karta hai
insert() → given index par add karta hai
extend() → ek list me dusri list ke elements jodta hai
'''

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)   # ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")
print(fruits)   # ['apple', 'orange', 'banana', 'cherry']

more_fruits = ["kiwi", "mango"]
fruits.extend(more_fruits)
print(fruits)   # ['apple', 'orange', 'banana', 'cherry', 'kiwi', 'mango']


# remove

"""
 Removing Elements

remove() → first occurrence delete karega
pop() → last item (ya specific index) hataega
clear() → puri list khali kar dega
"""

numbers = [1, 2, 3, 4, 5]

numbers.remove(3)
print(numbers)   # [1, 2, 4, 5]

numbers.pop()
print(numbers)   # [1, 2, 4]

numbers.pop(0)
print(numbers)   # [2, 4]

numbers.clear()
print(numbers)   # []


# searching ya checking bol sakte ho
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)   # True
print("mango" in fruits)    # False


# sort methods
numbers = [40, 10, 20, 30]

numbers.sort()
print(numbers)   # [10, 20, 30, 40]

numbers.reverse()
print(numbers)   # [40, 30, 20, 10]


# copy a list
a = [1, 2, 3]
b = a.copy()
print(b)   # [1, 2, 3]

# repetition 
a = [1, 2]
result = a * 3
print(result)

# len()
numbers = [10, 20, 30, 40]
print(len(numbers))   # total items

# max()
numbers = [5, 20, 10, 50]
print(max(numbers))   # sabse bada element

# main()
numbers = [5, 20, 10, 50]
print(min(numbers))   # sabse chhota element

# sum()
numbers = [10, 20, 30]
print(sum(numbers))   # sabhi numbers ka sum

# list()
text = "ABC"
converted = list(text)
print(converted)
















