a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("And the last one: "))
def maximum(a, b, c):
    if a>b and a>c:
        return 'The largest number is', a
    elif b>a and b>c:
        return 'The largest number is', b
    else:
        return 'The largest number is', c

print(maximum(a,b,c))