character=input("Enter a character : ")
b=ord(character)

if (b>=65 and b<=90):
    lc=b+32
    c={character:lc}
    print(c)
else:
    print("Not an uppercase")