
# Write a program which accept number from user and print its numbers line.
#Input : 4
#Output : -4 -3 -2 -1 0 1 2 3 4 

def main():

	no=int(input("Enter the number :"))

	i=-no
	while i<=no:
		print(str(i)+"\t",end = '')
		i=i+1


if __name__=="__main__":
	main()