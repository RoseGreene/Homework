import random
player1 = input("Enter your name: ")
player2 = input("Enter your name: ")
my_list = []
my_list.append(player2)
my_list.append(player1)
first_player = random.choices(my_list)

if first_player[0] == player1:
    print(player1 + ", you are the First player, and " + player2 + " is the Second player.")
else:
    print(player2 + ", you are the First player, and " + player1 + " is the Second player.")

game = ["-", "-", "-",
	    "-", "-", "-",
	    "-", "-", "-"]

for i in range(9):
	def board():
		print(game[0] + " | " + game[1] + " | " + game[2])
		print(game[3] + " | " + game[4] + " | " + game[5])
		print(game[6] + " | " + game[7] + " | " + game[8])

    if i%2==0:
        print("First player!")
        def typing1():
            place = int(input("where do you want to print 1-9: "))
            symbol = input("print X: ")
            game[place - 1] = symbol
    else:
        print("Second player!")
        def typing2():
            place = int(input("where do you want to print 1-9: "))
            symbol = input("print O: ")
            game[place - 1] = symbol


    def playing():
        board()
        typing1()
        typing2()

    
    typing1()
    playing()
    typing2()




