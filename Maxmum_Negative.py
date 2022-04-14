def fun(n):
  i=0
  max=n[0]
  while i<len(n):
    if n[i]>max:
      max=n[i]
    i=i+1
  return max
print(fun([-4,-5,-4,-1,-2,-5]))
