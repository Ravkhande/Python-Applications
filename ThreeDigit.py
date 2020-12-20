
# Not complete 

#  Accept N numbers from user and display all such numbers which contains
# 3 digits in it.
# Input : N : 6 
# Elements : 8225 665 3 76 953 858
# Output : 665 953 858 

def ThreeDigit(arr,no):

    iCnt=0
    for i in range(0,no):
        No=arr[i]
        temp=arr[i]
        while No!=0:
            Digit=No%10
            No=No//10
            if No==0:
                iCnt+=
                break
                
        if No==0 and iCnt==:
            print(arr[i])     
     
        

            
def main():
     arr=[]

     size=int(input("Enter the N value : "))

     print("Enter the N Elements : ")
     for x in range(0,size):
         item=int(input())

         arr.append(item)

     print(arr)

     ThreeDigit(arr,size)



if __name__=="__main__":
    main()


