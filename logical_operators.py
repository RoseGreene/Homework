a = input("What is your favorite color? ")
b = input("What color is the sky? ")
c = input("Which color's frequency is the shortest? ")

print("The fact that all this colors are the same is", bool(a==b and b==c and a==c))
print("The fact that there are the same colors in your answers is", bool(a==b or a==c or b==c))