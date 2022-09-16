def fun(a,b):
    for i in a:
        if a[i] not in b:
            print(a[i])
            break
    
fun([2,1,2],[1,1])
    