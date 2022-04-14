# 13..Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

nums = [0,1,0,3,12]
i=0
a=[]
b=[]
while i<len(nums):
    if nums[i]!=0:
        a.append(nums[i])
    elif nums[0]==0:
        b.append(nums[i])
    i=i+1
# print(a)
# print(b)
print(a+b)