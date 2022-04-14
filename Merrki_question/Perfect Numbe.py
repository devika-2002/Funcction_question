def perfect_num(): 
    num =int (input ("enter the number:="))
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum=sum+i
        i=i+1
    if num==sum:
        print("this is parfect number",sum)
    else:
        print("this is not parfect number",sum)
perfect_num()