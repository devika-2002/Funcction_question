def prime_or_Not(num):
    if num>1:
        for i in range(2,num):
            if (num%1)==0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"num")
                break
            else:
                print(num,"is a prime number")
        else:
            print(num,"is not a prime number")
prime_or_Not(406)