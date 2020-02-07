text = input("write something: ")
a = text[0]
lenth = len(text)
print(a + text[1:len(text)].replace(a, "$"))