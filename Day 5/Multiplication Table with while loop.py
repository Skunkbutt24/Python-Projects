number = int(input("Enter the number for which you want to generate the table: "))
upto = int(input("Enter the range till which you want to generate the table: "))
print("Here is your multiplication table:")
n=1
while upto>=n:
    print(f"{number}X{n}={number*n}")
    n+=1
    
    
    
