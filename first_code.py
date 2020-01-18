#input variables
first_name = input("What's your name?: ")
last_name = input("Please, say your last name. ")
age = input("How old are you?: ")
country = input("Where are you from?: ")

#making some space
print("    ")

#smth crazy
print("Hello " + first_name + " " + last_name + "!")
print("I know that you are " + age + " years old.")
print("And you are from " + country + ".")

#some space
print("   ")
print("Yes, I know everything about you! ^_^")

#we need some space
print("    ")

#types
print(type(first_name))
print(type(last_name))
print(type(age))
print(type(country))

print("    ")
#convert to its own type
print(type(int(age)))
