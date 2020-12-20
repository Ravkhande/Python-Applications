
#Write a program which accepts N from user and print all odd numbers up to N.
#Input : 18
#Output : 1 3 5 7 9 11 13 


def main():

	no=int(input("Enter the number : "))

	i=1
	while i<=no:
		if (i%2)!=0:
			print(str(i)+"\t",end = '')

		i=i+1




if __name__=="__main__":
	main()



