#Python Raw String

PyStr='Hi'
print(PyStr)

PyStr='Hi\nHello'
print(PyStr)

PyStr='Hi\nWelcome'
print(len(PyStr))

PyStr='Hi\nWelcome'
print(PyStr)
print(len(PyStr))
print(PyStr[2])
print(PyStr[3])
print(PyStr[0:7])
print(PyStr[-4:-6])

PyStr=R'Hi\nWelcome'
print(PyStr)

#PyStr='Hi\xHello'  #SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \xXX escape
print(PyStr)

PyStr="Hello Sateesh"
print(PyStr)
PyStr=U"Hello Sateesh"
print(PyStr)
print(len(PyStr))

PyStr=U"Hello\nSateesh"
print(PyStr)
print(len(PyStr))
print(PyStr[0])
print(PyStr[9])
print(PyStr[0:7])
print(PyStr[-10:-6])

PyStr=R"I\nam\nlucky"
print(PyStr[0:5])
print(PyStr[-7:-2])