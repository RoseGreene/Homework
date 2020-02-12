file1 = open("text1.txt")
for i in file1:
    print(min(i.split()))
file1.close()
