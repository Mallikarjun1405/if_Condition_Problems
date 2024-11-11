#97,101,105,111,117 - lowercase vowels
#65,69,73,79,85 - uppercase vowels

character=input("Enter a character : ")
b=ord(character)

if b==97 or b==101 or b==105 or b==111 or b==117 or b==65 or b==69 or b==73 or b==79 or b==85:
    c=b+1
    d=chr(c)
    print("Next character :",d)
else:
    print("Not a vowel")
