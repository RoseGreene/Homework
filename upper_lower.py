text = input("Write something with upper and lower letters: ")
def letters(text):
	upper=0
	lower=0
	for i in text:
		if i.isupper()==True:
			upper+=1
		else:
			lower+=1
	print("You have " + str(upper) + " upper letters in your text and " + str(lower) + " lowers.")
letters(text)