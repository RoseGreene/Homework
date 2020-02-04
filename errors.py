while True:
    try:
	    mark = int(input("what's your mark?"))
	    break
    except:
	    print("write it with numbers")
if mark>=35:
   print("Cograts! You're accepted as a full stack developer!")
else:
	print("try again. next time you will success!")