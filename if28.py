#a="0"
#print(ord(a))

character=input("Enter a character : ")
b=ord(character)

if (b>=65 and b<=90) or (b>=97 and b<=122):
    c={character:b}
    print(c)
else:
    print("Not an alphabet")