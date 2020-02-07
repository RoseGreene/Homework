num1 = int(input("Choose a number from 0 to 5: "))
num2 = int(input("Choose another one: "))
addition = num1 + num2
print("The sum of this numbers is greater than 5:", bool(addition > 5))
print("The sum of this numbers is equal to 5: ", bool(addition == 5))
print("The sum of this numbers is less than 5: ", bool(addition < 5))