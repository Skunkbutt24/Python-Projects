logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print(logo)
import random
print("Welcome to the number guessing game. Let's get started.\nI will generate a random number between 1-100. You have to guess that number.\nYou will have chances according to the difficulty.")
chosen_number = random.randint(1, 100)
chances = 0
while True:
    difficulty = input("What would be your difficulty? (Easy, Medium, Hard)\n").lower()
    if difficulty == "easy":
        chances = 15
    elif difficulty == "medium":
        chances = 10
    elif difficulty == "hard":
        chances = 5
    else:
        print("Invalid difficulty selection. Please try again.")
        continue 
    print(f"You have {chances} chances to guess the right number.")   
    while chances > 0:
        guess = int(input("Your guessed number: "))        
        if guess < 1 or guess > 100:
            print("Invalid input. Your guess should be between 1-100.")
            continue      
        if (guess - chosen_number) > 10:
            print("Too High!!!!!!!")
        elif (chosen_number - guess) > 10:
            print("Too Low!!!!!!")
        elif 0 < abs(guess - chosen_number) <= 10:
            print("Almost close!!!!!!")
        elif guess == chosen_number:
            print(f"Congratulations !!!!!\nYou got the right number. The number was {chosen_number}.")
            break
        chances -= 1
        print(f"You have {chances} chances left.")
    if chances == 0:
        print(f"You ran out of chances. The number was {chosen_number}.")
    break 
print("Thanks for using my program. Bye !!!!")


