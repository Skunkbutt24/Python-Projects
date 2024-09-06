print('This program will show you the sum of even numbers from "X" to "Y"\nLet\'s start ......')
num1=int(input("What is the first number ?\n-----> "))
num2=int(input("What is the last number ?\n-----> "))
sum=0
original_num1=num1
while num2>=num1:
    if num1%2==0:
        sum+=num1
    num1+=1
print(f"The sum of even numbers from {original_num1} to {num2} is : {sum}")


