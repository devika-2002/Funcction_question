# Q13.Write a function to check if a number is even or not.
def even_num(a):
    i=0
    while i<len(a):
        if a[i]%2==0:
            print("even",a[i])
        else:
            print("not",a[i])
        i=i+1
even_num([1,2,3,4,5,6])