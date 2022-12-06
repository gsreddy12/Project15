#len()

PyStr="Hello sateesh"
print(len(PyStr))
PyStr='Hi\nSateesh'   #In Unicoade string, other than the characters like escape sequences \
                      # special characters consider as only one character
print(len(PyStr))
PyStr=R'Hi\nSateesh'  #In Raw string, each and every thing consider as one character
print(len(PyStr))
PyStr='Hi\nSateesh_~~~~$%^&*'
print(len(PyStr))

print("-----------------------")

#join()

PyList=['1','2','2.3','4','5',"6"]
sep='-->'
print(sep.join(PyList))
str1="Hi s tring"
sep1='%%%'
print(sep1.join(str1))

print("-----------------------")

#max()

PyStr="abcd"
print(max(PyStr))  # It returns the character of highest ASCII value in that string
PyStr="abcddcba"
print(max(PyStr))
PyStr="Maximum"
print(max(PyStr))
PyStr="%^&&$123"
print(max(PyStr))

print("-----------------------")

#min()

PyStr="abcd"
print(min(PyStr))  # It returns the character of lowest ASCII value in that string
PyStr="abcddcba"
print(min(PyStr))
PyStr="Maximum"
print(min(PyStr))
PyStr="%^&&$123"
print(min(PyStr))