#WAP to check whether given input is divisible by 2 and 6. If the condition is satisfied, convert the given 
# number into a complex number.

a=int(input("Enter a value : "))

if a%2==0 and a%6==0:
    a=complex(a)
    print(a)
else:
    print("a value is not divisible by 3 and 5")