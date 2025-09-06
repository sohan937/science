# write a program to input eight number from the user and display all the unique number once
s=set()
n=int(input("enter number 1:"))
s.add(n)
n=int(input("enter number 2:"))
s.add(n)
n=int(input("enter number 3:"))
s.add(n)
n=int(input("enter number 4:"))
s.add(n)
n=int(input("enter number 5:"))
s.add(n)
n=int(input("enter number 6:"))
s.add(n)
n=int(input("enter number 7:"))
s.add(n)
n=int(input("enter number 7:"))
s.add(n)
print(s)


'''
output:
enter number 1:1     
enter number 2:3
enter number 3:5
enter number 4:6
enter number 5:7
enter number 6:8
enter number 7:9
enter number 7:10
{1, 3, 5, 6, 7, 8, 9, 10}
'''