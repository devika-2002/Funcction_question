def even(n):
    if n>9:
        i=0
        sum=0
        rem=0
        while i<n:
            rem=n%10
            sum=sum+rem
            n=n//10
        print(sum)
        return even(sum)
    else:
        if n%2==0:
            print("even")
        else:
            print("odd")
n=int(input("enter the number:"))
even(n)