#rjust()

PyStr='PYTHON'
length=10
fillchar='*'
print(PyStr.rjust(length,fillchar))
PyStr='PYTHON is very good programming'
length=50
fillchar='&'
print(PyStr.rjust(length,fillchar)) #it retuns left side

print("-----------")

#ljust

PyStr='PYTHON'
length=10
fillchar='*'
print(PyStr.ljust(length,fillchar))
PyStr='PYTHON is very good programming'
length=50
fillchar='&'
print(PyStr.ljust(length,fillchar))  #it returns right side

print("-----------")

#center()


PyStr='PYTHON'
length=10
fillchar='*'
print(PyStr.center(length,fillchar))
PyStr='PYTHON is very good programming'
length=50
fillchar='&'
print(PyStr.center(length,fillchar)) #it returns equal parts

print("-----------")
