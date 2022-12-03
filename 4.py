#Sting Built-in Methods

#capitalize()

str1="naresh i technologies"
print(str1.capitalize())
str2="HELLO HOW ARE U123"
print(str2.capitalize())
str3=" naresh i technologies"
print(str3.capitalize())   #Whatever the character, starting of a string that should be considered as Capital

print("-----------------------")

#isdigit()

str1="PYTHON"
print(str1.isdigit())
str2="12345"      #It considers only digits
print(str2.isdigit())
str3="PYTHON786"
print(str3.isdigit())
str4="12PYTHON"
print(str4.isdigit())
str5="123_"
print(str5.isdigit())
str6="0"
print(str6.isdigit())
str7="0.9"     #It considers only intergers
print(str7.isdigit())
str8="0.9"
format(str8,'d')
print(str8.isdigit())