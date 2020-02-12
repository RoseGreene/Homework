my_file = open("text.txt", "a")
new_list = []
num = int(input("How many items do you want to enter: "))
for i in range(num):
	a = input("Write an item: ")
	new_list.append(a)
my_file.writelines(new_list)
my_file.close()