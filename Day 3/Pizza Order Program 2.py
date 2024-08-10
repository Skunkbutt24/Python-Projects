print("Hi, Welcome to self checkout menu. Let's get started.")
size=input("What would be the size of your pizza ? : ")
pepperoni=input("Do you want pepporoni ? : ")
cheese=input("Do you want extra cheese ? : ")
S=15
M=20
L=25
bill=0
if size == "S":
    bill=15
elif size == "M":
    bill=20
elif size == "L":
    bill=25
if pepperoni == "Y":
    if size == "S":
       bill+=2
    elif size == "M" or size == "L":
        bill+=3
if cheese == "Y":
    bill+=1
print(f"Your total bill is {bill}$")


