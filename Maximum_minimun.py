a=[2,3,4,8,5,9,1,7]
def mix():
    i=0
    max=0
    min=a[0]
    while i<len(a):
        if a[i]>max:
            max=a[i]
        elif a[i]<min:
            min=a[i]
        i=i+1
    print(max)
    print(min)
mix()
            