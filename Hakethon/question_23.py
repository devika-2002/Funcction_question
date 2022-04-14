# 23. Counting parameters
# Define a function param_count that takes a variable number of parameters. The function should return the number of arguments it was called with.
# For example, param_count() should return 0, while param_count(2, 3, 4) should return 3.

def my(n):
    i=0
    c=0
    while i<len(n):
        c=c+1
        i=i+1
    return c
print(my([2,3,4]))