my_dict = {"color":"black", "wave":"electromagnetic", "particle":"photon", "theory":"quantum"}
i = input("search the key: ")
if i in my_dict:
	print("We have that key in our dictionary!")
else:
	print("We don't have that key in our dictionary!")
