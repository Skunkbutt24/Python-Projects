print("What's your weight")
weight=int(input())
print("What's your height")
height=float(input())
bmi=round((weight/(height**2)),2)
if bmi<18.5:
    print(f"Your bmi is {bmi} and you are underweight ")
elif bmi>18.5 and bmi<=25:
    print(f"Your bmi is {bmi} and you have a normal weight ")
elif bmi>25 and bmi<=35:
    print(f"Your bmi is {bmi} and you are slightly overweight ")
elif bmi>35:
    print(f"Your bmi is {bmi} and you are obese ")
    