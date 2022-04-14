#1..# o/p:-["A","A","A","B","B","B","C","C","C","D","A","A","B"]
def fun():   
    a="AAABBBCCCDAAB"
    i=0
    b=[]
    while i<len(a):
        if a not in []:
            b.append(a[i])
        i=i+1
    print(b)
fun()

#2...# O/P:-["A","B","C","D","A","B"]
def fun():   
    a="AAABBBCCCDAAB"
    i=0
    j=1
    b=[]
    while j<len(a):
        if a[i]!=a[j]:
            b.append(a[i])
        j+=1
        i=i+1
    b.append(a[i])
    print(b)
fun()