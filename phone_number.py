while True:
    try:
	    number = int(input("enter your phone number: "))
	    break
    except:
	    print("Phone number should be written with numbers!")
if str(number).startswith("93") or str(number).startswith("94") or str(number).startswith("77"):
	print(" You use VivaCell operatore!")
elif str(number).startswith("55"):
	print("You use Ucom!")
elif str(number).startswith("99"):
	print("You are Beeline user!")




