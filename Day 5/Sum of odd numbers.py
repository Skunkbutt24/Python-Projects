print('This program will show you the sum of odd numbers from "X" to "Y"\nLet\'s start ......')
num1=int(input("What is the first number ?\n-----> "))
num2=int(input("What is the last number ?\n-----> "))
sum=0
for num in range(num1,num2 + 1):
    if num%2!=0:
        sum+=num
print(f"The sum of odd numbers from {num1} to {num2} is : {sum}")


