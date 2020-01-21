number = int(input("Enter a number: "))
x = number%5
y = number%11
print("The fact that your number is divisible by 5 and 11 is", bool(x==0 and y==0))