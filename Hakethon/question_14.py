# 14..Power of Four
# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.
#  Example 1:
# Input: n = 16
# Output: true
# Example 2:
# Input: n = 5
# Output: false
# Example 3:
# Input: n = 1
# Output: true

def squre():
    i=0
    a=int(input("enter the number"))
    while i<4:
        if a==4:
            print("true",a*4)
            break
        else:
            print("false")
            break
    i=i+1
squre()