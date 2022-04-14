def max():
    a=int(input("enter the number:-"))
    b=int(input("enter the number:-"))
    c=int(input("enter the number:-"))
    if a>b and a>c:
        print("maximum:-",a)
    elif b>c and b>a:
        print("maximum:-",b)
    else:
        print("maximum:-",c,)
max()