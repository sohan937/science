# Create an empty dictionaey .allow gour students enter their favourite language ass value and use kay as their names.Assume that the names are unique

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
'''
output:
enter the name:sagar
eneter the language name:python
enter the name:rohan
eneter the language name:english
enter the name:siddharth
eneter the language name:bpsc
{'sagar': 'python', 'rohan': 'english', 'siddharth': 'bpsc'}
'''