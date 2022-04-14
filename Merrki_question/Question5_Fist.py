# 3 aur 5 ke multiples => 3, 5, 6, 9, 10
#:-33 
def number(user):
    i=0
    sum=0
    while i<=user:
        if i%3==0 or i%5==0:
            sum=sum+i
        i=i+1
    print(sum)
number(10)
                
    