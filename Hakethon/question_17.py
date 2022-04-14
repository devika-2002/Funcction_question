# 17. Capital indexes
# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

a="HeLlO"
i=0
b=[]
while i<len(a):
    if a[i].isupper()==True:
        b.append(i)
    i=i+1
print(b)