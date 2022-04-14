def vote():
    age=int(input("enter the number"))
    i=0
    while i<=age:
        if 18<age:
           print("you are eligible")
           break
        else:
             print("not eligible ")
             break
    i=i+1
vote()