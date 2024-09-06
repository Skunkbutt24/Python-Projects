print("This program will show you numbers sequentially")
num2=int(input("What is the first digit ? :"))
num1=int(input("What is the last digit ? :"))
print("Here are the numbers sequentially-\n")
for num in range(num2,num1-1,-1):
    print(num)