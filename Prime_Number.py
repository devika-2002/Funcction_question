b=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
prime=[]
i=0
while i<len(b):
    j=1
    c=0
    while j<b[i]:
        if b[i]%j==0:
            c=c+1
        j=j+1
    if c==1:
        prime.append(b[i])
    i=i+1
print(prime)