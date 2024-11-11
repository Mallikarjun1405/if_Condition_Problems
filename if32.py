character=input("Enter a character : ")
b=ord(character)

if (b>=65 and b<=90) or (b>=97 and b<=122):
    print(int(b))
else:
    print("Not a character")