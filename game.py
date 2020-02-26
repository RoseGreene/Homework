game = ["-", "-", "-",
	    "-", "-", "-",
	    "-", "-", "-"]

for i in range(9):
	def play_game():
		print(game[0] + " | " + game[1] + " | "+ game[2])
		print(game[3] + " | " + game[4] + " | "+ game[5])
		print(game[6] + " | " + game[7] + " | "+ game[8])


	def typing():
		place = int(input("where do you want to print 1-9: "))
		symbol = input("what do you want to print X or O: ")
		game[place-1] = symbol

	def playing():


		play_game()
		typing()


	typing()
	playing()
	play_game()	







