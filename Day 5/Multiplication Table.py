number = int(input("Enter the number for which you want to generate the table: "))
upto = int(input("Enter the range till which you want to generate the table: "))
for n in range(1,upto+1):
    print(f"{number} X {n} = {number * n}")
