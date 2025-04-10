#defines the function f(x) and comes up with an output
def f(x):
	return x**3 + 8

#main function, inputs 9 as 
def main():
	x = 9
	result = f(x)
	print(result) #prints out the output of f(9)

	#If f(x) > 27, prints Yay
	if result > 27:
		print("YAY!")

#runs the program
if __name__ == "__main__":
	main()
