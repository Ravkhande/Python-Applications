
# Write a program which accept string from user and count number of
# capital characters.
# Input : “Marvellous Multi OS”
# Output : 4 

def CountCapital(str):
    iCnt=0

    for strs in str:
        if strs>='A' and strs<='Z':
            iCnt+=1

    return iCnt


def main():
    print("Enter the string : ")
    str=input()
    
    Result=CountCapital(str)

    print("Number of capital charaters is : ")
    print(Result)


if __name__=="__main__":
    main()