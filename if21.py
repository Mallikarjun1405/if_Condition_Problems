a=int(input("Enter a value : "))

if (a>=45 and a<=125) and (a%4==0 and a%5==0 and a%2==0):
    b=chr(a)
    print("ASCII value of",a,"is",b)

else:
    print('a value not satisfies the condition (between 45 to 125 and divisible by 4 and 5 and even)')