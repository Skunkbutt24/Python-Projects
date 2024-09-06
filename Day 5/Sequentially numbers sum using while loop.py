print("This program will show you the sum of total sequent numbers")
num1=int(input("What's the first digit ? :"))
num2=int(input("What's the last digit ? :"))
sum=0
original_num1=num1
while num2>=num1:
    sum+=num1
    num1+=1
print(f"The sum of {original_num1} to {num2} is : {sum} ")
