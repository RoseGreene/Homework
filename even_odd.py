limit = int(input("Say some limit: "))
def showNumbers(limit):
	for i in range(limit + 1):
		if i % 2 == 0:
			print (str(i), "EVEN")
		elif i % 2 != 0:
			print(str(i), "ODD")
showNumbers(limit)

