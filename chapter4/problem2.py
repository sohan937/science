# write a program to accept marks of 6 students and display them in a sorted manner.
marks=[]
f1=int(input("Enter marks here:"))
marks.append(f1)
f2=int(input("Enter marks here:"))
marks.append(f2)
f3=int(input("Enter marks here:"))
marks.append(f3)
f4=int(input("Enter marks here:"))
marks.append(f4)
f5=int(input("Enter marks here:"))
marks.append(f5)
marks.sort()
print(marks)


'''
output:Enter marks here:52
Enter marks here:32
Enter marks here:25
Enter marks here:98
Enter marks here:14
[14, 25, 32, 52, 98]

'''