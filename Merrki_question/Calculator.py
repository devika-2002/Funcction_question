def multipal(num1,num2):
    i=0
    b=[]
    while i<len(num1):
        a=num1[i]*num2[i]
        b.append(a)
        i=i+1
    print(b,end=" ")
multipal([5, 10, 50, 20], [2, 20, 3, 5])  