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
game_images = [rock, paper, scissors]
game_names = ["Rock", "Paper", "Scissors"]

user_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n")) - 1
if user_choice < 0 or user_choice >= 3:
    print("You typed an invalid number, you lose!")
else:
    print(f"Your move is {game_names[user_choice]}:\n{game_images[user_choice]}")
    computer_choice = random.randint(0, 2)
    print(f"Computer chose {game_names[computer_choice]}:\n{game_images[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose")
