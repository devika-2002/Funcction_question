from itertools import count


n=[1,5,4,2,5,5,4,5,5]
i=0
count=0
max=0
while i<len(n):
  if n[i]>max:
    max=n[i]
  i=i+1
j=0
while j<len(n):
  if max==n[j]:
    count+=1
  j+=1 
print("maximum:",max,"count:")
 

