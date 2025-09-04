#  String is a data type in Python that represents a sequence of characters enclosed within single quotes (' '), double quotes (" "), or triple quotes (''' ''' / """ """).
# String ek immutable data type hai (iska content badla nahi ja sakta directly).
# string slicing:A  string slicing in python can be sliced for getting a part of the strings


# example 
name="sagar"   # isme indexing 0,1,2,3,4  hai ya r=-1index,a=-2,g=-3,a=-4,s=-5.     iska total length 5 hai 
print(name[0:2])   #output:sa   o index  se start hoga 2 ko chhor dega
# print(name[5]    index error dega
print(name[-4:-1])   #output:aga     negative wala ko phle positiveb kr denge
print(name[1:4])   #output:aga
print(name[1:])      #iska mtlb hai [1:5] jitna length rahega utna tak le lega
print(name[:])     #iska output [0:5]  sagar
print(name[:4])    #iska output [0:4]



        #   slicing skip value:[start,end,step]  isme end ko include nhi krenge
a = "0123456789"
print(a[1:7:3])    #output:14





