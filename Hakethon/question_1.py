# You are provided an array A of size N  that contains non-negative integers.
# Your task is to determine whether the number that is formed by selecting the 
# last digit of all the N numbers is divisible by 10
# .Note: View the sample explanation section for more clarification.
# Input format
# First line: A single integer N denoting the size of array A
# Second line: N space-separated integers.
# Output format
# If the number is divisible by 10, then print Yes. Otherwise, print No
# Sample Input
# 5
# 85 25 65 21 84
# Sample Output
# No
# Explanation
# The last digit of 85 is 5
# The last digit of 25 is 5
# The last digit of 65 is 5
# The last digit of 21 is 1
# The last digit of 84 is 4
# .Therefore the number formed is 55514 which is not divisible by 10.

list=[85,25,65,21,84]
i=0
a=[]
while i<len(list):
    if list[i]>0:
        a.append(list[i]%10)
        j=0
        while i<len(a):
            if a[j]%10==0:
                print("yes")
                break
            else:
                print("no")
                break
        j=j+1
    i=i+1
    break
# print(a)

