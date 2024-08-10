import random
import string
name = input("What's your name? : ")
print(f"Welcome Mr. {name} to our automatic password generator program.")
yes_no = input("Do you want to create a random password?\n(Type Yes and No) : ").lower()
if yes_no == "yes":
    capital_letters = string.ascii_uppercase
    small_letters = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation
    digits_no = int(input("How many digits do you want? : "))
    capital_no = int(input("How many capital letters do you want? : "))
    small_no = int(input("How many small letters do you want? : "))
    numbers_no = int(input("How many numbers do you want? : "))
    symbols_no = int(input("How many symbols do you want? : "))
    if (capital_no + small_no + numbers_no + symbols_no) == digits_no:
        password = [] 
        for char in range(capital_no):
            password.append(random.choice(capital_letters))
        for char in range(small_no):
            password.append(random.choice(small_letters))
        for char in range(numbers_no):
            password.append(random.choice(numbers))
        for char in range(symbols_no):
            password.append(random.choice(symbols))
        random.shuffle(password)
        shuffled_list = ''.join(password)  
        print(f"Here is your randomly generated password: {shuffled_list}")
    else:
        print("The sum of letters, numbers, and symbols may exceed or be less than the total digits.\nPlease check your input again.......")
else:
    print(f"It's ok, Mr.{name}\nSorry for wasting your time.")
