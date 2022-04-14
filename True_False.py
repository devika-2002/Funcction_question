
# list=[1,2,3,3]
list=[1,1,1,1]
i=0
a=[]
while i<len(list):
    if list[i]==list[0]:
        a.append(list[i])
    i=i+1
if a==list:
    print(True)
else:
    print(False)
    

