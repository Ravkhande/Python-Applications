
#  Accept N numbers from user and display summation of digits of each
# number.
# Input : N : 6
# Elements : 8225 665 3 76 953 858
# Output : 17 17 3 13 17 21 

def DigitsSum(arr,no):
    
    Sum=0
    for x in range(0,no):
        No=arr[x]

        while No !=0:
            Digit=No%10
            Sum=Sum+Digit
            No=No//10    # here // is called as floor which is used to round off values if value is 7.5 then it becomes the 7

        print(str(Sum) , end='' +"\t")
        Sum=0
    
 
    
def main():

    arr=[]
    size=int(input("Enter the N value : "))

    print("Enter the N elements : ")
    for x in range(0,size):
        item=int(input())
        arr.append(item)

    print(arr)

    DigitsSum(arr,size)


if __name__=="__main__":
    main()



