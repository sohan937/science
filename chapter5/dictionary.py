# Dictionary is a key collection of keys value pairs.
marks={
    "sagar":100,
    "Sohan":56,
    "Bala":23
}
print(marks,type(marks))    # output:{'sagar': 100, 'Sohan': 56, 'Bala': 23} <class 'dict'>


print(marks["sagar"])      # output:100

print(marks.get("sagar"))      # output:100
print(marks.get("sagar2"))     #output:None
print(marks["sagar2"])          #output:KeyError: 'sagar2' 


# properties of python dictionaries
'''
1.  it is unordered.
2.  it is mutable
3.  it is indexed
4.  can't contain duplicate values
'''