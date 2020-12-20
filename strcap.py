
# Write a program which accept string from user and copy capital
# characters of that string into another string.
#  Input : “Marvellous Multi OS” 
# Output : “MMOS” 

def StrCpyCap(strs):
    arr=[]
    list1=list(strs)

    length=len(list1)
    i=0
    while i<length:
        if list1[i]>='A' and list1[i]<='Z':
            arr.append(list1[i])
        i+=1

    str=listToString(arr)

    print(str,end='')




def listToString(arr):

    str=" "    # initailization of empty string

    # traverse in the string 
    for i in arr:
        str+=i

    return str
     

def main():

    print("Enter the string : ")
    str=input()

    StrCpyCap(str)


if __name__=="__main__":
    main()