def list():
    i=0
    a=[]
    while i<10:
        i+=1
        a.append(i)
        if i%2==0:
            print("even",i)
        else:
            print("odd",i)
        
    print(a)
list()


