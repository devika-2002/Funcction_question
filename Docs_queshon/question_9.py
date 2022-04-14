# Q9.Write a Python program to generate and print a list of first and last 5
# elements where 
# the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).
def fun():
    i=0
    a=[]
    b=0
    while i<=30:
        b=i*i
        a.append(b)
        i=i+1
    print(a[1:6],a[25:])
fun()