# Q16.Print multiplication table of 12 using function.
# Q16.Print multiplication table of 12 using function.
def table():
    a=int(input("enter the number"))
    i=1
    j=12
    while i<a:
        print(i,"*",j,"=",i*j)
        i=i+1
table()