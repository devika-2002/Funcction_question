a=[10,20,30,40,10,10,20,30,20,50]
i=0
e=[]
while i<len(a):
    j=0
    c=0
    while j<len(a):
        if a[i]==a[j]:
            c=c+1
        j=j+1
        # if a[i]==a[j]:
        #     break
    e.append(c)
    i=i+1
print(e)
    