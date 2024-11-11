a=int(input("Enter a value : "))

if a%2==0:
    print('Not Odd')
else:
    a=str(a)
    a=tuple(a)
    print(a)