character=input("Enter a character : ")
b=ord(character)

if (b>=97 and b<=122):
    r=int(input("Number of times to replicate : "))
    c=character*r
    print(c)
else:
    print("Not a lowercase")