def even_odd():
    num=[1,2,3,4,5,6,7,8]
    i=0
    while i<len(num):
        if num[i]%2==0:
            print("Even_number:-",num[i])
        else:
            print("odd_number:-",num[i])
        i=i+1
even_odd()