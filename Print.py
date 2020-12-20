
#Write a program which accept number from user and print numbers till that
#number.
#Input : 8
#Output : 1 2 3 4 5 6 7 8 

def main():

	no=int(input("Enter the number : "))

	i=1
	while i<=no:
		print(str(i)+"\t",end = '')
		i=i+1


if __name__=="__main__":
	main()