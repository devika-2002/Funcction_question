#1..#string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish","Divyashish"]
# new_list = ["Rishabh", "Abhishek", "Divyashish"]
def fun(string_list):
    i=0
    a=[]
    while i<len(string_list):
        if string_list[i] not in a:
            a.append(string_list[i])
        i=i+1
    print(a)

fun(["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish","Divyashish"])