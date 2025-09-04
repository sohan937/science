# escape sequence character comprise to more than one character but represent one character whwn used within the strings
# agar aapko string me new line print krna hai to
a="sagar is a good boy \n he is very dishonest person"
print(a)

b="sagar is a good \"boy\""         #output:sagar is a good "boy"
print(b)

c="sagar is a good 'boy'"         #output:sagar is a good "boy"
print(c)

d='sagar is a good \'boy\''         #output:sagar is a good "boy"
print(d)

