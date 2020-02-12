file1 = open("text.txt")
file2 = open("text1.txt", "a")
for i in file1:
	file2.write(i)
file1.close()
file2.close()