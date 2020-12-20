
# Write a program which accept string from user and count number of
# small characters. 

# Input : “Marvellous”
# Output : 9


def CountSmall(str):
    iCnt=0
    for strs in str:
        if strs>='a' and strs<='z':
            iCnt+=1

    return iCnt


def main():

    print("Enter the string : ")
    str=input()

    Result=CountSmall(str)
    print("Number of small charaters is : ")
    print(Result)


if __name__=="__main__":
    main()