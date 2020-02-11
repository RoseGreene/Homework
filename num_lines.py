my_file = open("my_file.txt", "r")
count=0
for i in my_file:
	count+=1
print(count)
my_file.close()