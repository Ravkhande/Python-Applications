
# Write a program which 2 strings from user and concat second string
# after first string. (Implement strcat() function). 

# Input : “Marvellous Infosystems”
# “Logic Building”
# Output : “Marvellous Infosystems Logic Building” 


def StrCatX(str1,str2):
    
    str1+=' '
    for i in str2:     # same like for each loop
        str1+=i
        
    print(str1,end='')    # “Marvellous Infosystems Logic Building”     


def main():

    print("Enter the string 1 : ")
    str1=input()

    print("Enter the string 2 : ")
    str2=input()

    StrCatX(str1,str2)


if __name__=="__main__":
    main()