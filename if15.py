a=int(input("Enter a value : "))

if a%3==0 and a<30:
    b=a**2
    print("Square value of",a,"is",b)
else:
    print("a value not satisfies the condition (divisible by 3 and less than 30)")