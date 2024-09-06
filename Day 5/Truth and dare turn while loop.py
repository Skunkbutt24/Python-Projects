import random
print("Welcome to the Truth and Dare game.\nThis program will show you whose turn it is.")
people = int(input("How many people are there ?\n"))
names = []
n=1
while people>=n:
    names.append(input(f"Enter player number {n} name: "))
    n+=1
random_name=random.choice(names)
print(f"It's {random_name} turn.")
