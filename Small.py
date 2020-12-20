
#  Accept N numbers from user and return the smallest number.
 #Input : N : 6
 #Elements : 85 66 3 66 93 88
#Output : 3


def Minimum(arr,no):

    min=arr[0]
    for i in range(0,no):
        if min>arr[i]:
            min=arr[i]
    
    return min



def main():

    arr=[] 

    size=int(input("Enter the N value : "))

    print("Enter the N Elements :")
    for x in range(0,size):
        item=int(input())

        arr.append(item)

    print(arr)

    Ret=Minimum(arr,size)
    print("Smallest number is : " + str(Ret))



if __name__=="__main__":
    main()
