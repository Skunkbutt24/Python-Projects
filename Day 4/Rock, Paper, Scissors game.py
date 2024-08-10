logo = '''
██████████████████████████
█▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄███
██─▄─▄█─██─█─███▀██─▄▀████
▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
█████████████████████████████████
█▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀███
██─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
██████████████████████████████████████████████
█─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀█─▄▄▄▄█
█▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print(logo)
move_images = [rock, paper, scissors]
move_names = ["Rock", "Paper", "Scissors"]
while True:
    print("Welcome to my Rock, Paper, Scissors game. Let's get started.")
    user_choice = int(input("Type 1 for Rock, Type 2 for Paper, Type 3 for Scissors:\n"))
    computer_choice = random.randint(1, 3)
    if user_choice < 1 or user_choice > 3:
        print("Invalid Number.")
        start_over = input("Do you want to start over? (yes/no)\n").lower()
        if start_over != "yes":
            print("Bye!")
            break
    else:
        print(f"Your move is {move_names[user_choice - 1]}:\n{move_images[user_choice - 1]}")
        print(f"Computer's move is {move_names[computer_choice - 1]}:\n{move_images[computer_choice - 1]}")
        if user_choice == computer_choice:
            print("It's a draw.")
        elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
            print("You win!")
        else:
            print("You lose!")
        start_over = input("Do you want to start over? (yes/no)\n").lower()
        if start_over != "yes":
            print("Bye!")
            break
