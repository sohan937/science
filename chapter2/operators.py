# Operators are symbols or keywords in Python that are used to perform operations on variables and values.


                #   Types of Operators in Python
'''
Arithmetic Operators → Mathematical calculations

+ (Addition)

- (Subtraction)

* (Multiplication)

/ (Division → float result)

// (Floor Division → integer result)

% (Modulus → remainder)

** (Exponentiation → power)

'''

a = 10
b = 3
print(a + b)   # 13
print(a % b)   # 1
print(a ** b)  # 1000
print(a/b)      #3.3333
print(a//b)      #3



                  # Relational  Comparison Operators → Compare values, return True/False
'''
== (equal to)

!= (not equal to)

> (greater than)

< (less than)

>= (greater or equal)

<= (less or equal)

'''

print(5 > 3)   # True
print(5 == 3)  # False


           # Logical Operators → Combine conditions


"""
and
or
not

"""

x = 5
print(x > 2 and x < 10)  # True
print(not(x > 2))        # False


                # Assignment Operators → Assign values (with/without operation)
"""
= (simple assignment)

+= (add and assign)

-= (subtract and assign)

*= (multiply and assign)

/=, //=, %=, **=

"""

a = 5
a += 3   # same as a = a + 3
print(a) # 8



                   # Bitwise Operators → Work on bits (0,1)
"""
& (AND)
| (OR)
^ (XOR)
~ (NOT)
<< (left shift)
>> (right shift)
"""
a = 100    
print(~a)  # 101   digital electronics me hmne padha h signed magnitude representation

                   # 5. Left Shift (<<)
'''
 Bits ko left shift karta hai, aur right side me 0 bhar deta hai.
a << n → a ka binary n bits left shift hota hai.
Ye multiply by 2^n ke barabar hai.
'''   
a = 5   # 0101
print(a << 1)  # 10
print(a << 2)  # 20

 
           # 5. right Shift (<<)
'''
Bits ko right shift karta hai, aur left side me 0 bhar deta hai (positive numbers ke liye).
a >> n → a ka binary n bits right shift hota hai.
Ye divide by 2^n (floor value) ke barabar hai.

'''

a = 20   # 10100
print(a >> 1)  # 10
print(a >> 2)  # 5
print(a >> 3)  # 2
print(a >> 4)  # 1
print(a >> 5)  # 0
print(a >> 6)  # 0
print(a >> 7)  # 0
print(a >> 8)  # 0





                     # Membership Operators → Check if a value exists in a sequence (list, string, etc.)

"""
1. in
2. not in
"""
nums = [1,2,3,4]
print(2 in nums)      # True
print(5 not in nums)  # True




# Identity Operators → Compare memory location (object identity)
'''
is
is not
'''
x = [1,2,3]
y = x

z = [1,2,3]

print(x is y)      # True (same object)
print(x is  z)      # False (same value but different object)










