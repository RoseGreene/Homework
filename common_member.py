my_list1 = [ 99, 53, "juice", "YSU"]
my_list2 = ["apple", 56, "home"]
def lists(my_list1, my_list2):
	for i in my_list1:
		for g in my_list2:
			return bool(i == g)
	           
	
print(lists(my_list1, my_list2))

