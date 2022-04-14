            # DUPLICATES_NUMBER
# Q5.Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List (O/P): [1, 2, 3, 4, 5].
def fun():  
    list=[1,2,3,3,3,3,4,5]
    i=0
    a=[]
    while i<len(list):
        if list[i] not in a:
            a.append(list[i])
        i=i+1
    print(a)
fun()