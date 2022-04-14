def total(num1,num2):
    add=num1+num2
    return add
def diff(num1,num2):
    sub=num1-num2
    return sub
def product(num1,num2):
    multiply=num1*num2
    return multiply
def divisble(num1,num2):
    divisble=num1/num2
    return divisble
def mod(num1,num2):
    remainder=num1%num2
    return remainder
def flo(num1,num2):
    flo=num1//num2
    return flo
def operator():
    op=input("inter operator")
    if op=="+":
        print(total(num1,num2))
    elif op=="-":
        print(diff(num1,num2))
    elif op=="*":
        print(product(num1,num2))
    elif op=="/":
        print(mod(num1,num2))
    elif op=="%":
        print(num1%num2)
    elif op=="//":
        print(num1//num2)
num1=int(input("Enter the number:-"))
num2=int(input("Enter the number:-"))
operator()
        