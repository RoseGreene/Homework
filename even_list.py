my_list = [23, 46, 74,9, 18]
new_list = []
def evens(new_list):
	for i in my_list:
		if i%2==0:
			new_list.append(i)
	return new_list
print(evens(new_list))