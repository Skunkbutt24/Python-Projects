print("Enter your number :")
number=int(input())
if number>=60 and number<=100:
    print("You are passed")
if number>=60 and number<=70:
    print("You have got B rating")
elif number>70 and number <=80:
    print("You have got A rating")
elif number>80 and number<=90:
    print("You have got A rating")
elif number>90 and number<=100:
    print("You have got A+")
else:
    print("You are failed")
