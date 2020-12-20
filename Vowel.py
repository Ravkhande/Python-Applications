
#  Write a program which accept string from user and check whether
# it contains vowels in it or not.
# Input : “marvellous” 
# Output : TRUE 
# Input : “Demo”
# Output : TRUE
# Input : “xyz”
# Output : FALSE
# 


def ChkVowel(str):

    for strs in str:
        if strs=='A' or strs=='a' or strs=='E' or strs=='e' or strs=='I' or strs=='i' or strs=='O' or strs=='o' or strs=='U' or strs=='u':
            break

    if strs=='A' or strs=='a' or strs=='E' or strs=='e' or strs=='I' or strs=='i' or strs=='O' or strs=='o' or strs=='U' or strs=='u':
        return True
    else:
        return False
        


def main():

    bRet=False

    print("Enter the string : ")
    str=input()

    bRet=ChkVowel(str)
    if bRet==True:
        print("string contains vowel in it ")
    else:
        print("string not contains vowel in it")


if __name__=="__main__":
    main()
