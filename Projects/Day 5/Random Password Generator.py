import random
import string
name = input("What's your name ? : ")
print(f"Welcome Mr. {name} to our automatic password generator program.")
yes_no = input("Do you want to create a random password ?\n(Type Y for Yes and N for No) : ")
if yes_no == "Y" or yes_no == "y":
    capital_letters = string.ascii_uppercase
    small_letters= string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation
    digits_no = int(input("How many digits do you want ? :"))   
    capital_no = int(input("How many capital letters do you want ? :"))
    small_no = int(input("How many small letters do you want ? :"))
    numbers_no = int(input("How many numbers do you want ? :"))
    symbols_no = int(input("How many symbols do you want ? :"))
    if (capital_no + small_no + numbers_no + symbols_no) == digits_no:
        password = ""
        for char in range(0, capital_no):
            password += random.choice(capital_letters)
        for char in range(0, small_no):
            password += random.choice(small_letters)
        for char in range(0, numbers_no):
            password += random.choice(numbers)
        for char in range(0, symbols_no):
            password += random.choice(symbols)
        password_list = list(password)
        random.shuffle(password_list)
        shuffled_list = ""  
        for char in password_list:
            shuffled_list += char
        print(f"Here is your random generated password: {shuffled_list}")
    else:
        print("The sum of letters, numbers, and symbols may exceed or be less than the total digits.\nPlease check your input again.......")
else:
    print(f"It's ok, Mr.{name}\nSorry for wasting your time.")
