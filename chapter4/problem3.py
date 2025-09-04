# check that a type can't be changed in python
a=(32,234,"sagar")
a[2]="vidya"
print(a)


'''
because tuples are immutable
output":Traceback (most recent call last):
  File "c:\Desktop\science\chapter4\problem4.py", line 3, in <module>
    a[2]="vidya"
    ~^^^
TypeError: 'tuple' object does not support item assignment

'''