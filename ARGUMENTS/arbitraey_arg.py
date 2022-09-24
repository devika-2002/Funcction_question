# Arbitrary argument,*args   ????????

# def num(*a):
#     c=a+b
# print(num(1,2,3))


# def my(*a):
#     print(a)
# my(1,4,5,9)


def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")