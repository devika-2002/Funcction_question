# Q33. Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi > 30 return "Obese"
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
def fun():
    bmi=int(input("enter the number:-"))
    i=0
    while i<=bmi:
        if bmi>30:
            print("obese")
            break
        elif bmi<=18.5:
            print("Underweight")
            break
        elif bmi<=25.0:
            print("Normal")
            break
        elif bmi<=30.0:
            print("Overweight")
            break
    i=i+1
fun()
        