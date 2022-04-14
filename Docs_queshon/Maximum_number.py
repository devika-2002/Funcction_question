# Q2.Write a Python function to find the Max of three numbers.
def max_number():
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    c=int(input("enter the number"))
    if a>b and a>c:
        print("Maximum",a)
    elif b>c and b>a:
        print("Maximum",b)
    else:
        print("Maximum",c)
max_number()
