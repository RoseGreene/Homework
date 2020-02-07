text = input("write something: ")
if len(text) >=3:
    if text[-3:] == "ing":
        print(text + "ly")
    else:
        print(text + "ing")
else:
    print(text)