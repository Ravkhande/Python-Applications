
#  Accept N numbers from user and return the largest number.
# Input : N : 6
# Elements : 85 66 3 66 93 88
# Output : 93 

def Maximum(arr,value):

    max=arr[0]
    for i in range(0,value):
        if max<arr[i]:
            max=arr[i]
    
    return max


def main():

    Arr=[]

    no=int(input("Enter the N value : "))

    print("Enter the N elements: ")
    # 1st way #
    for i in range(0,no):
        item=int(input())
        Arr.append(item)
    
    print(Arr)

    Ret=Maximum(Arr,no)
    print("Largest number is : " + str(Ret))



if __name__=="__main__":
    main()