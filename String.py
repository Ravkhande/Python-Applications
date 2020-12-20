
print("Enter the string")
str=input()

print("3 ways to create string : ")
string1='Pratik'
string2="Pratik"
string3="'Pratik'"

print("Different methods of string : ")
print(type(str))
print(str.title())
print(str.upper())
print(str.lower())

str1='Pratik '
print("It will remove the white space at right side : " + str1.rstrip()) 

str2=' Pratik'
print("It will remove the white space at right side : " + str1.lstrip()) 

print("Entered string is : " + str)
print("Entered string is : " + string3)