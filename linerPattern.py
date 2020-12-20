

# Write a program which accept number from user and print that number of $ & *
#on screen.
#Input : 5
#Output : $ * $ * $ * $ * $ *
#Input : 3
#Output : $ * $ * $ *
#Input : -3
#Output : $ * $ * $ * 

def main():

	no=int(input("Enter the number : "))

	for i in range(no):
		print("$"+"\t"+"*"+"\t",end = '')


if __name__=="__main__":
	main()