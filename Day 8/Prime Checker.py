import math
number = int(input("This program will check whether the input prime or not.\nEnter the number: "))
prime = False 
if number > 1:
    prime = True 
    for i in range(2, int(math.sqrt(number)) + 1):# number**0.5
        if number % i == 0:
            prime = False
            break
if prime:
    print("It's a prime number.")
else:
    print("It's not a prime number.")
