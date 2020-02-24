my_list = []
new_list = []

class Target:

	def __init__(self, target):
		self.target = target

	def numbers(self):
		target = int(self.target)
		num = int(input("How many items do you want to enter: "))
		for i in range(num):
			n = int(input("enter a number: "))
			my_list.append(n)
		print(my_list)

		for i in range(len(my_list)):
			for j in range(len(my_list)):
				if (my_list[i]+my_list[j]) == target and i<j:
					print(my_list[i]+my_list[j])
					new_list.append(i)
					new_list.append(j)
		print(new_list)			

printed = Target(30)
print(printed.numbers())