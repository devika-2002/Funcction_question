n=int(input("Enter the number:-"))
m=int(input("Enter the number:-"))
a=[]
while n<=m:
    j=1
    sum=0
    while j<n:
        if n%j==0:
            sum+=1
        j=j+1
    if sum==1:
        a.append(n)
    n=n+1
print(a)