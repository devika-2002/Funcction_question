# Q14.Write a function to check if a number is prime or not.
def prime(a):
    i=0
    while i<len(a):
        j=1
        count=0
        while j<=a[i]:
            if a[i]%j==0:
                count=count+1
            j=j+1
        if count==2:
            print(a[i],"This is a prime number")
        else:  
           print(a[i],"This is not a prime number")
        i=i+1
prime([1,2,3,4,5,6,7,8,9])


