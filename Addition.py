

import Functions

def main():
    value1=int(input("Enter the number 1 : "))
    value2=int(input("Enter the number 2 : "))

    ret=Functions.Add(value1,value2)
    print("Addition is : ")
    print(ret)

    ret=Functions.Sub(value1,value2)
    print("Subtraction is : ")
    print(ret)

    ret=Functions.Mult(value1,value2)
    print("Multiplication is : ")
    print(ret)

    ret=Functions.Div(value1,value2)
    print("Division is : ")
    print(ret)


if __name__=="__main__":
    main()


