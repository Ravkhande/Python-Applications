
           # Tuple #
 # Note : tuple is constant or unchangeable and therefore it is not possible to add item in tuple  

def main():
    Myarray=("Pratik", "Sujata" , "Kavita" , "Mira" , "Savita")  # Tuple
    print(Myarray) 
    print(Myarray[1])
    print(Myarray[1:4])
    print(Myarray[1:])
    print(Myarray[:3])
    print(Myarray[-1])
    print(Myarray[-4:-1])

    # to change tuple values convert the tuple to list
    list1=list(Myarray)    # to convert the tuple to list  
    list1[1]="Topper"
    Myarray=tuple(list1)   # # to convert the list to tuple
    print(Myarray)

    # to check if item exist or not
    if "Topper" in Myarray:
        print("Yes it is present")

    print(len(Myarray))

    tuple2=("a", "b","c",1,2,3,3,4,3,3,3)
    tuple3=tuple2+Myarray
    print(tuple3)

    x=tuple2.count(3) # count function counts the number of times the particular value appers in tuple
    print(x)    # 5

    y=tuple2.index(4)   # it returns the index of specific value 
    print(y)    # 7

    del Myarray


if __name__=="__main__":
    main()