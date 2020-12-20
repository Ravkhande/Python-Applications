
# Accept N numbers from user and return the difference between largest
#and smallest number.
#Input : N : 6
#Elements : 85 66 3 66 93 88
#Output : 90 (93 -3) 

def Difference(arr,no):
    
    max=arr[0]
    min=arr[0]

    for i in range(0,no):
        if max<arr[i]:
            max=arr[i]

    for j in range(0,no):
        if min>arr[j]:
            min=arr[j]

    Diff=max-min
    return Diff


 
def main():
    
    arr=[]
    size=int(input("Enter the N value : "))

    for x in range(0,size):
        item=int(input())

        arr.append(item)

    Ret=Difference(arr,size)
    print("Difference between largest and smallest number is : " + str(Ret))



if __name__=="__main__":
    main()


