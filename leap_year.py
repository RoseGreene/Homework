year = int(input("Enter the year: "))
x = year % 4
print("The year you entered is leap: ", bool(x == 0))