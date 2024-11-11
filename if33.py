character=input("Enter a character : ")
a=ord(character)

if (a>=33 and a<=47) or (a>=58 and a<=64) or (a>=91 and a<=96) or (a>=123 and a<=126):
    print(character,"(special symbol) :",a,"(ASCII value)")
else:
    print("Not a special symbol")