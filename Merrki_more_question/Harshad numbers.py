num=int(input("enter the any number:-"))
sum=0
var=num
while (var>0):
    digit=var%10
    sum=sum+digit
    var=var//10
if num%sum==0:
    print("Harshad_number:-",sum)
else:
    print("not a Harshad_number:-",sum)