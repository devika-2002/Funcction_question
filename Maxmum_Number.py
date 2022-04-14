# mathad ka used nhi krke maxmum ka 

def fun(n):
  i=0
  max=0
  while i<len(n):
    if n[i]>max:
      max=n[i]
    i=i+1
  return max
print(fun([1,5,4,5,2,5]))


