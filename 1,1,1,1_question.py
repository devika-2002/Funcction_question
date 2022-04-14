def fun(list):
    a=1
    b=[]
    i=0
    while i<len(list):
        c=list[i-a+1]
        b.append(c)
        a=a+1
        i=i+1
    print(b)
fun([1,2,3,4,5])
    
    
