text="hello world"
print(text.upper())    #output:HELLO WORLD




word="SAGAR"
print(word.lower())    #output:sagar

word1="hello world"
print(word1.title())    #output:Hello World

word2="hello world"
print(word2.capitalize())    #output:Hello world

word3=" hello world"
print(word3.capitalize())    #output:hello world   isme gaur krke dekho space ke wajah se first letter captal nhi hua


word4=" hello sagar "
print(word4.strip())     #output:hello sagar space hata deta hai right or left side dono ka

word5=" hello sagar "
print(word5.lstrip())    #hello sagar sirf left side ka strip hata dega

word6=" hello sagar "
print(word6.rstrip())      #hello sagar sirf right side ka strip hata dega

word7="hello world"
print(word7.replace("world","python"))   #output:hello python


data="apple,banana,mango"
print(data.split(","))        #string ko list me tod dega ['apple','banana','mango']

items=['apple','banana','mango']   #list ko string me join kr deta hai output: apple-banana-mango
print("-".join(items))


word8="hello world"
print(word8.find("world"))       # output 6 substring ka index dega nhi milega to -1 dega


print("banana".count("a"))
# Output: 3


word9="hello"
print(word9.startswith("h"))      #output :True


word10="hello"
print(word10.endswith("o"))      #output :True

print("Hello".isalpha())   # True
print("Hello123".isalpha()) # False

print("12345".isdigit())  # True
print("12a45".isdigit()) # False


print("Hello123".isalnum()) # True
print("Hello 123".isalnum()) # False (space है)


print("   ".isspace()) # True    sirf space rahega tb hi true
print("  a  ".isspace()) # False



print("HeLLo".swapcase())
# Output: "hEllO"


print("42".zfill(5))    #number ko 0 se fill krega
# Output: "00042"

print("Hi".center(10, "-"))
# Output: "----Hi----"
