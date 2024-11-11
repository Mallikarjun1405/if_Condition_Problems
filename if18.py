a=int(input("Enter a value : "))

if a<0 or a%2==0:
    b=str(a)
    print(b[-1])
else:
    print('a value not satisfies the condition (negative or even number)')