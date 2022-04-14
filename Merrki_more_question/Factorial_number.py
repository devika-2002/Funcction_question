def fun(num):
    fact=1
    while num>0:
        fact=fact*num
        num=num-1
    return  fact
num=int(input("enter the number:-"))
print("this is factorial number:-",fun(num))
 