
# l1 =[7,2,4,3] 
# l2 = [5,6,4]
# i=0
# a=[]
# while i<len(l1):
#     a.append(l1[i])
#     j=0
#     b=[]
#     while i<len(l2):
#         b.append(l2[j])
#         j=j+1
#     i=i+1
# print(a+b)
# # # print(b)

   
def num_list(num1,num2):
    i=-1
    b=[]
    while i>=len(num1)-1:
        # a=num1[i]+num2[i]
        b.append(num1[i])
        j=0
        a=[]
        while j<len(num2):
            a.append(num2)
            j=j+1
        i=i-1
    print(b)
num_list([7,2,4,3],[5,6,4])

# list=[2,4,6,3,8,9,3]
# # O/P:-[[2,4],[6,3],[8,9]]
# i=0
# b=[]
# while i<len(list)-1:
#     c=[]
#     c.append(list[i])
#     c.append(list[i+1])
#     b.append(c)
#     i=i+2
# print(b)    