character=input("Enter a character : ")
b=ord(character)

if (b>=65 and b<=90):
    c={character:b}
    print(c)
else:
    print("Not an uppercase")