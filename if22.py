a=int(input("Enter a value : "))

if (a>=25 and a<=100) and (a%4==0 and a%5==0):
    b=a*5
    print(a,"Multiplied with 5 is",b)

else:
    print('a value not satisfies the condition (between 25 to 100 and divisible by 4 and 5)')