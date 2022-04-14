def sum(a):
    i=0
    b=[]
    sum=0
    while i<len(a):
        sum=sum+a[i]
        b.append(sum)
        i=i+1
    print(b)
sum([1,2,3,4,5])