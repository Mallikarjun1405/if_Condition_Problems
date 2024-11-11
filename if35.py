a=int(input("Enter a value : "))
b=int(input("Enter b value : "))

if a==10 or b==10 or a+b==10:
    sum=a+b
    result=sum**2
    print(result)
else:
    print("a and b values not satisfies the condition (a or b equals to 10) or a plus b equals to 10")