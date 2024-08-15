import random
print("Welcome to the Truth and Dare game.\nThis program will show you whose turn it is.")
people = int(input("How many people are there ?\n"))
names = []
for x in range(1, people + 1):
    name = input(f"Enter Player Number {x} name: ")
    names.append(name)
turn = random.choice(names)
print("This is your turn:", turn)
