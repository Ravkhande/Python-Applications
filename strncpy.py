
#  Write a program which accept string from user and copy the
# contents of that string into another string. (Implement strncpy() function)

# Input : “Marvellous Multi OS”
#            10 
# Output : “Marvellous


def StrNCpyX(strs,no):

    list1=list(strs)        # to convert string into array(list)
    i=0
    while i<no:
        print(list1[i] , end ='')
        i+=1

    

    


def main():

    print("Enter the string : ")
    str=input()

    print("Enter the number : ")
    no=int(input())

    StrNCpyX(str,no)



if __name__=="__main__":
    main()