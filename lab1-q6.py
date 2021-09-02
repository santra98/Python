a = str(input("enter a string"))
temp = a
str =""
for i in a:
    str = i + str
if temp == str:
    print("The given string is a palindrome")
else:
    print("Not palindrome")

