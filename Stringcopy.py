
# Write a program which accept string from user and copy the
# contents of that string into another string. (Implement strcpy() function) 

# Input : “Marvellous Multi OS” 
# Output : “Marvellous Multi OS” in another string 

def StrCpyX(strs):

    str1=strs
    print(str1, end = '')



def main():
    print("Enter the string : ")
    str=input()

    StrCpyX(str)


if __name__=="__main__":
    main()
