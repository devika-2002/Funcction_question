# Q38. Your task is to create function is Divided By (or is_divide_by) to check if
# an integer number is divisible by each out of two arguments.
# A few cases:
# (-12, 2, -6)  ->  true
# (-12, 2, -5)  ->  false
# (45, 1, 6)    ->  false
# (45, 5, 15)   ->  true
# (4, 1, 4)     ->  true
# (15, -5, 3)   ->  true

def  divisible():
    n=int(input("enter the number:-"))
    a=int(input("Enter the number:-"))
    b=int(input("Enter the number:-"))  
    if n%a==0 and n%b==0:
        print("true")
    else:
        print("false")  
divisible()
