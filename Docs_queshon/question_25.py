# Q25. Given a list of numbers, write a Python program to count positive and 
# negative numbers in a List using function.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3
def neg_pos(list):   
    i=0
    count=0
    count1=0
    a=[]
    while i<len(list):
        if list[i]>0:
            count=count+1
        elif list[i]<0:
            count1=count1+1
        i=i+1
    print("pos=",count,",","Neg=",count1)
neg_pos([2,-7,5,-64,-14])



# list = [2, -7, 5, -64, -14]    
# i=0
# count=0
# count1=0
# a=[]
# while i<len(list):
#     if list[i]>0:
#         count=count+1
#     elif list[i]<0:
#         count1=count1+1
#     i=i+1
# print("pos=",count,",","Neg=",count1)
