# o/p:-true ya false me jo integar me hai aana chahiye true nhi to false
a=["a","b",1,3,"g",5,"f",7,4,12,9]
i=0
while i<len(a):
    if type(a[i])==int:
        print(True)
    else:
        print(False)
    i=i+1