import random
print("This program will show you a random odd number. Let's get started.")
start=int(input("What would be the starting point ? : "))
end=int(input("What would be the ending point ? : "))
odd=[num for num in range(start,end+1) if num%2!=0]
random_odd=random.choice(odd)
print(f"Here is the random odd number: {random_odd}")