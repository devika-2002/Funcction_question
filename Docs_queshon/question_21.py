# Q21.What is the output of the following code snippet?
# O/P:-C. The program has a runtime error because the local variable ‘num’ 
# referenced before assignment.


num = 1
def func():
    num = num + 3
    print(num)

func()
print(num)

