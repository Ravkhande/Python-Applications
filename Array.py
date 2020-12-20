# In python Arrays is called as collection and there are four collections in python as follows
# 1. list -  List is a collection which is ordered and changeable , and it Allows duplicate members 
# 2. Tuple - Tuple is a collection which is ordered but unchangeable , and it Allows the duplicate members
# 3. Set - Set is collection which is unordered and unindexed. No duplicate members is allowed
# 4. Dictionary - is a collection which is unordered, changeable and indexed. No duplicate members 

def main():

    Myarray=["Pratik", "Sujata" , "Savita" , "Kavita"]      # List

    print(Myarray[1])     # Sujata
    print(type(Myarray))  # list
    print(Myarray[-1])    # Kavita
    print(Myarray[1:3])     # ['Sujata', 'Savita']
    print(Myarray[:3])     #['Pratik', 'Sujata', 'Savita']
    print(Myarray[1:])     #['Sujata', 'Savita', 'Kavita']
    print(Myarray[-3:-1])   #['Sujata', 'Savita']  


    # change item value
    Myarray[2]="Mira"
    print(Myarray)     # ['Pratik', 'Sujata', 'Mira', 'Kavita']

    # Loop through a List
    for x in Myarray:
        print(x)

    # check if item exists
    if "Mira" in Myarray:
        print("Yes it is present in list ")

                  # various list methods 
    # to calculate length of list
    print(len(Myarray))

    # to add item at end of list used append
    Myarray.append("Ravkhande")
    print(Myarray)   # ['Pratik', 'Sujata', 'Mira', 'Kavita', 'Ravkhande']

    # to add item at specified index used insert method
    Myarray.insert(1,"Topper")
    print(Myarray)    # ['Pratik', 'Topper', 'Sujata', 'Mira', 'Kavita', 'Ravkhande']

    # make a copy of a list with the copy() method
    Newlist=Myarray.copy()
    print(Newlist)   # ['Pratik', 'Topper', 'Sujata', 'Mira', 'Kavita', 'Ravkhande'] 

    # remove method removes the specified item
    Myarray.remove("Topper")
    print(Myarray)  # ['Pratik', 'Sujata', 'Mira', 'Kavita', 'Ravkhande']

    # another way to make a copy of alist with the list() method :
    newlist=list(Myarray)
    print(newlist)   # ['Pratik', 'Sujata', 'Mira', 'Kavita', 'Ravkhande']

    # to join two lists
    list3=Myarray+newlist
    print(list3)     # ['Pratik', 'Sujata', 'Mira', 'Kavita', 'Ravkhande', 'Pratik', 'Sujata', 'Mira', 'Kavita', 'Ravkhande']

    # pop method removes the specified index, (or the last item if index is not specified)
    Myarray.pop()
    print(Myarray)     # ['Pratik', 'Sujata', 'Mira', 'Kavita']

    # del keyword removes the specified index
    del Myarray[0]
    print(Myarray)     # ['Sujata', 'Mira', 'Kavita']

    # clear() metheod empties the list
    Myarray.clear()
    print(Myarray)    # []

    # del keyword can also delete the list completely 
    del Myarray

      

if __name__=="__main__":
    main()