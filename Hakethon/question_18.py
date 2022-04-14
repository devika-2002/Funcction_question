# 18. Middle letter
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".

a="abc"
# a="abcbg"
i=0
c=""
while i<len(a):
    if len(a)%2==0:
         print(repr(c))
         break
    else:
        c=len(a)//2
        print(repr(a[i+c]))
        break
    i=i+1
