
# Write a program which accept string from user and copy small
# characters of that string into another string.
# Input : “Marvellous multi OS”
# Output : “arvellous multi”

def StrCpySmall(str):

    str1=" "    # initalization of empty string

    # Taverse in the empty string
    for i in str:     # it is same as foreach loop in java
        if i>='a' and i<='z':
            str1+=i
        elif i==' ':
            str1+=i
    
    print(str1,end='')


def main():

    print("Enter the string : ")
    str=input()

    StrCpySmall(str)


if __name__=="__main__":
    main()