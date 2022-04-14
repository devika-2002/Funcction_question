#5..Chef and Chocolates
# Chef wants to gift C chocolates to Botswal on his birthday. However, he has only X chocolates with him. The cost of 1 chocolate is Y rupees.
# Find the minimum money in rupees Chef needs to spend so that he can gift C chocolates to Botswal.
# Input Format
# First-line will contain T, the number of test cases. Then the test cases follow.
# Each test case contains a single line of input, three integers C, X, and Y.
# Output Format
# For each test case, output in a single line answer, the minimum money in rupees Chef needs to spend.
# Sample Input 1 
# 7 5 5
# 10 1 1
# Sample Output 1 
# 10
# 9

# Explanation
# Test Case 1: Chef has to gift a total of 7 chocolates out of which he has 5 chocolates. Thus, Chef needs to buy 2 more chocolates, which costs him 10 rupees.
# Test Case 2: Chef has to gift a total of 10 chocolates out of which he has 1 chocolate. Thus, Chef needs to buy 9 more chocolates, which costs him 9 rupees.


a=int(input("enter the number:-"))
b=int(input("enter the number:-"))
i=0
while i<a:
    c=a-b
    n=int(input("enter the how much rupish"))
    print(c*n)
    break
i=i+1




# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=input("enter the number")
# d=a-b
# e=d*c
# print(e)