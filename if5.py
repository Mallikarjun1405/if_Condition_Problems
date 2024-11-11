#

a=int(input("Enter a value : "))

if a%3==0 or a%5==0:
    a=list(str(a))
    print(a)
else:
    print("a value is not divisible by 3 or 5")