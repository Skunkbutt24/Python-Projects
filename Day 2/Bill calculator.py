print("Welcome to Tip Calculator program.\nLet's get started.")
total_bill=float(input("What's the total bill ?\n"))
tip_percentage=float(input("How much tip do you want to add ?\n"))
person=int(input("How many people do you wanna split between ?\n"))
ans=(total_bill+(total_bill*tip_percentage/100))/person
if ans.is_integer():
    print(f"So, each person has to pay {ans}$")
else:
    print(f"So, each person has to pay {ans: .2f}$")
answer=round((total_bill+(total_bill*tip_percentage/100))/person,2)
print(answer)