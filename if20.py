a=int(input("Enter a value : "))

if a%4==0 and a%2==0:
    c=chr(a)
    print("ASCII value of",a,"is",c)

else:
    print('a value not satisfies the condition (divisible by 4 and even number)')