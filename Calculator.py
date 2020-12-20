

import Function

def main():
    value1=int(input("Enter the number 1 : "))
    value2=int(input("Enter the number 2 : "))

    ret=Function.Add(value1,value2)
    print("Addition is : ")
    print(ret)

    ret=Function.Sub(value1,value2)
    print("Subtraction is : ")
    print(ret)

    ret=Function.Mult(value1,value2)
    print("Multiplication is : ")
    print(ret)

    ret=Function.Div(value1,value2)
    print("Division is : ")
    print(ret)


if __name__=="__main__":
    main()


