print("What is the toatl bill ? - ")
bill=float(input())
print("How much tip do you want to give ? - ")
tip=int(input())
print("How many people to split the bill ? - ")
people=int(input())
result=round(((bill+bill*(tip/100))/people),2)
print(f"Each person has to pay - ${result}")

