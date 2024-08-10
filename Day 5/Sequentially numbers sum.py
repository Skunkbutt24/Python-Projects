print("This program will show you the sum of total sequent numbers")
num1=int(input("What's the first digit ? :"))
num2=int(input("What's the last digit ? :"))
sum=0
for num in range(num1,num2+1):
    sum+=num
print(f"The sum of {num1} to {num2} is : {sum} ")
