def even_sum():
    a=input("enter the number")
    b=input("enter the number")
    i=0
    sum=0
    while i<len(a):
        sum=int(a[i])+int(b[i])
        i=i+1
    print(sum)
    if sum%2==0:
        print("even")
    else:
        print("odd")
even_sum()
