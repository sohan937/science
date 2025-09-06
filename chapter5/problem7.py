# If the names of two friends are same ; what will happen to the program in problems
d={}
name=input("enter the name:")
lang=input("eneter the language name:")
d.update({name:lang})
name=input("enter the name:")
lang=input("eneter the language name:")
d.update({name:lang})
name=input("enter the name:")
lang=input("eneter the language name:")
d.update({name:lang})
print(d)
# value update ho jaayegi
'''
output:enter the name:vidya
eneter the language name:python
enter the name:vidya
eneter the language name:english
enter the name:sohan
eneter the language name:physics
{'vidya': 'english', 'sohan': 'physics'}


'''