file1 = open("rtext.txt", "r")
n = int(input("which line do yop want to read: "))
f = file1.readlines(n)
print(f)
file1.close()