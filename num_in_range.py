num = int(input("Enter a number: "))
def number(num):
	if num in range(125):
		print("Your number is in the range.")
	else:
		print("Your number is not in the range.")
number(num)