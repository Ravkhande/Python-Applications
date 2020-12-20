# Write a program which accept string from user and return
# difference between frequency of small characters and frequency of
# capital characters. 

# Input : “MarvellouS”
# Output : 6 (8-2)

def Difference(str):

    smcount=0
    capcount=0

    for strs in str:
        if strs>='A' and strs<='Z':
            capcount+=1
        elif strs>='a' and strs<='z':
            smcount+=1

    diff=smcount-capcount
    return diff


def main():

    print("Enter the string : ")
    str=input()

    Result=Difference(str)
    print("Difference between frequency of small characters and frequency of capital characters is : ")
    print(Result)


if __name__=="__main__":
    main()