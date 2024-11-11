#middle character

a=int(input("Enter a value : "))

if (a<125 and a>60):
    b=str(a)
    c=len(b)//2
    print(a[c])

else:
    print('a value not satisfies the condition (less than 125 and greater than 60)')