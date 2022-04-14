# [5,4,0,1,9] iska sum krna hai o/p:-[14,5]
l=[5,4,0,1,9]
i=0
b=[]
while i<len(l):
    d=l[i]+l[-(i+1)]
    b.append(d)
    if len(b)==2:
        break
    i=i+1
print(b)