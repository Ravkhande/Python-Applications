
#Write a program which accept N and print first 5 multiples of N.
#Input : 4
#Output : 4 8 12 16 20 


def MultipleDisplay(value):


	for i in range(0,5):
		print(str(value)+"\t",end = '')
		value=value+4
		



def main():

	no=int(input("Enter the number : "))
	MultipleDisplay(no)


if __name__=="__main__":
	main()

