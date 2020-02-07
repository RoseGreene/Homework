stock_items = ["book", "pen", "pencil", "bag", "hippo"]
num = int(input("How many items do you want to buy? "))
available =[]
not_available=[]
for i in range(num):
    a = input("What do you want to buy: ")
    if a in stock_items:
    	available.append(a)
print("You can buy", available)
	    