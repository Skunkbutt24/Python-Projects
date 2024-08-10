import random
print("This program will show you a random number. Let's get started.")
start=int(input("What would be the starting point ? : "))
end=int(input("What would be the ending point ? : "))
number=[num for num in range(start,end+1)]
random_number=random.choice(number)
print(f"Here is your random number: {random_number}")