# Q10.Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):
# "4",  "5" --> "9"
# "34", "5" --> "39"
# Notes:
# If either input is an empty string, consider it as zero.
def add():
    a=input("Enter the number:-")
    b=input("Enter the number:-")
    if a ==""  and b == "":
        print("0")
    elif a=="":
        print(b)
    elif b=="":
        print(a)
    else:
        print(str(int(a)+int(b)))
add()

