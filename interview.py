# i=1
# while i<=6:
#     print("*"*i)
#     i=i+1

# n=int(input("enter the number"))
# i=0
# sum=0
# while i<=n:
#     n1=int(input("enter the number"))
#     sum=sum+n1
#     i=i+1
# print(sum)

# list_queshtion
# # o/p:-[[6,1],[5,2],[4,3]] aayega
# list=[1,2,3,4,5,6]
# i=0
# j=-1
# a=[]
# while i<len(list)/2:
#     a.append(list[j])
#     a.append(list[i])
#     i=i+1
#     j=j-1
# print(a)
        
# o/p [[5,25],[10,20][7,23]]
list=[20,5,10,23,25,7]
c=30
i=0
a=[]
while i<len(list):
    j=0
    b=[]
    while j<len(list):
        if list[i]+list[j]==c and list[j]>list[i]:
            b.append(list[i])
            b.append(list[j])
            a.append(b)
        j=j+1
    i=i+1
print(a)

