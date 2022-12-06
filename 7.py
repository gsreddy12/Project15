#replace()

str1="Hello How are you"
print(str1.replace("you","U"))
print(str1.replace("are","R"))

str2="Hello How are are you"
#print(str1.replace("you","U"))
print(str2.replace("are","R"))
print(str2.replace("are","R",1))

print("-----------------------")

#title()

PyStr="this is powerful python"
print(PyStr.title())

print("-----------------------")

#zfill()

PyStr="PYTHON"
print(PyStr.zfill(10))
print(PyStr.zfill(15))
print(PyStr.zfill(ord('a')))

print("-----------------------")

#isalnum()

PyStr="2009"
print(PyStr.isalnum())
str5="this"
print(str5.isalnum())
str="this string example ....... wow" #it won't allow the sepcial operators
print(str.isalnum())
p=""
print(p.isalnum())