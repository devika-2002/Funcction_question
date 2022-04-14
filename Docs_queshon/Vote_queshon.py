# Q17. Write a function to tell user if he/she is able to vote or not.
# ( Consider minimum age of voting to be 18. )
def vote():
    n=int(input("enter the number"))
    if n>18 :
        print("she is able to vote")
    else:
        print("she is not able to vote")
vote()