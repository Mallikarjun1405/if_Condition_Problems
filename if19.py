a=int(input("Enter a value : "))

if (a<0 or a%2!=0) and a%4==0:
    b=a**3
    print("Cube value of",a,"is",b)
else:
    print('a value not satisfies the condition (negative or odd number and divisible by 4)')