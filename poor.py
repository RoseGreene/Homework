text = input("Write your opinion about our lovely vaRchApet: ")
b = text.find("not")
if text.index("not") < text.index("poor"):
    print(text.replace(text[b:], "good"))



		