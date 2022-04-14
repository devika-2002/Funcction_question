# 22. Palindrome
# A string is a palindrome when it is the same when read backwards.
# For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".
# Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.



# name=["n","i","t","i","n"] krna hai
name="bob"
i=-1
n=[]
while i>=-len(name):
    n.append(name[i])
    i-=1
if n==name:
    print("this is pallindrome")
else:
    print("this is not pallindrome")