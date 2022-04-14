# def fun(a,b):
#     c=a+b
#     print(c)
# # fun(89,9)
# fun(10,20)

# def fun(x,y):
#     c=x+y
#     print("Result is:=",c)
# fun (x=90,y=87)
# # fun(y=40,x=30)

# def person(name,age):
#     print(name)
#     print(age)
# print(age=24,name="devika")
 
# def pw(x,y):
#     z=x**y
#     print(z)
# pw (5,2)


# def add(a,b):
#     return a+b
# def sub(c,d):
#     print(add(5,5))
#     return c-d
# def mul(e,f):
#     print(sub(5,12))
#     return e*f
# print(mul(3,10))
    
    
# def add(a,b):
#     c=a+b
#     return c
# def num(c=7,d=2):
#     print(add(2,4))
#     return c+d
# def num1():
#     print(num(3,2))
#     e=3
#     f=4
#     x=e+f
#     print(x)
# def num2(a,b):
#     num1()
#     return a+b
# print(num2(4,5))
    

# def fun (*a):
#     print(a)
# fun("devika",2,1.6)


 
# def fun(n):
#   i=0
#   max=0
#   while i<len(n):
#     if n[i]>max:
#       max=n[i]
#     i=i+1
#   return max
# print(fun([1,5,4,5,2,5]))

# negative ???????????????????????????????????

# def fun(n):
#   i=0
#   max=0
#   while i<len(n):
#     if n[i]>max:
#       max=n[i]
#     i=i+1
#   return max
# print(fun([-1,-5,-4,-5,-2,-5]))

# n=[-1,-5,-4,-2,-5,-4,-5,-5]
# i=0
# max=0
# while i<len(n):
#   if n[i]>max:
#     max=n[i]
#   i=i+1
# print(max)
 
 
# def fun(n):
#   i=0
#   max=0
#   while i<len(n):
#     if n[i]>max:
#       max=n[i]
#     i=i+1
#   return max
# print(fun([1,5,4,5,2,5]))


# name=input("enter the name:-")
# a=["amisha","manpreet","rani","rekha"]
# i=0
# while i<len(a):
#     if a[i][0] in name:
#         print(a[i])
#     i=i+1
        
        
name=input("enter the name:-")
a=["amisha","manpreet","rani","rekha"]
i=0
b=[]
while i<len(a):
    if a[i][0] in name:
        b.append(a[i])
    i=i+1
print(b)
        
