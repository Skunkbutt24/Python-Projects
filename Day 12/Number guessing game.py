logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print(logo)
import random
print("Welcome to the number guessing game. Let's get started.\nI will generate a random number between 1-100. You have to guess that number.\nYou will have chances according to the difficulty.")
while True:
    chosen_number=random.randint(1,101)
    chances=0
    difficulty=input("What would be your difficulty ? (Easy, Medium, Hard)\n").lower()
    if difficulty=="easy":
        chances+=15
        print(f"You have {chances} chances to guess the right number.")
        while True:
            guess=int(input("Your guessed number: "))
            if (guess-chosen_number)>10 and (guess-chosen_number)<=100:
                print("Too High!!!!!!!")
                chances-=1
                print(f"You have {chances} chances left.")
                if chances==0:
                    print(f"You ran out of chances. The number was {chosen_number}.")
                    break
            elif (chosen_number-guess)>10 and (chosen_number-guess)<=100:
                print("Too Low!!!!!!")
                chances-=1
                print(f"You have {chances} chances left.")
                if chances==0:
                    print(f"You ran out of chances. The number was {chosen_number}.")
                    break
            elif ((guess-chosen_number)<=10 and (guess-chosen_number)>0) or ((chosen_number-guess)<=10 and (chosen_number-guess)>0):
                print("Almost close!!!!!!")
                chances-=1
                print(f"You have {chances} chances left.")
                if chances==0:
                    print(f"You ran out of chances. The number was {chosen_number}.")
                    break
            elif (guess-chosen_number)>100 or (chosen_number-guess) or guess.is_integer():
                print("Invalid input. Try again. Your guess should be between 0-100.")
                continue
            else:
                print(f"Congratulations !!!!!\nYou got the right number. The number was {chosen_number}.")
                break
        break
    elif difficulty=="medium":
        chances+=10            
        print(f"You have {chances} chances to guess the right number.")
        while True:
            guess=int(input("Your guessed number: "))
            if (guess-chosen_number)>10 and (guess-chosen_number)<=100:
                print("Too High!!!!!!!")
                chances-=1
                print(f"You have {chances} chances left.")
                if chances==0:
                    print(f"You ran out of chances. The number was {chosen_number}.")
                    break
            elif (chosen_number-guess)>10 and (chosen_number-guess)<=100:
                print("Too Low!!!!!!")
                chances-=1
                print(f"You have {chances} chances left.")
                if chances==0:
                    print(f"You ran out of chances. The number was {chosen_number}.")
                    break
            elif ((guess-chosen_number)<=10 and (guess-chosen_number)>0) or ((chosen_number-guess)<=10 and (chosen_number-guess)>0):
                print("Almost close!!!!!!")
                chances-=1
                print(f"You have {chances} chances left.")
                if chances==0:
                    print(f"You ran out of chances. The number was {chosen_number}.")
                    break
            elif (guess-chosen_number)>100 or (chosen_number-guess):
                print("Invalid input. Try again. Your guess should be between 0-100.")
                continue
            else:
                print(f"Congratulations !!!!!\nYou got the right number. The number was {chosen_number}.")
                break
        break
    elif difficulty=="hard":
        chances+=5            
        print(f"You have {chances} chances to guess the right number.")
        while True:
            guess=int(input("Your guessed number: "))
            if (guess-chosen_number)>10 and (guess-chosen_number)<=100:
                print("Too High!!!!!!!")
                chances-=1
                print(f"You have {chances} chances left.")
                if chances==0:
                    print(f"You ran out of chances. The number was {chosen_number}.")
                    break
            elif (chosen_number-guess)>10 and (chosen_number-guess)<=100:
                print("Too Low!!!!!!")
                chances-=1
                print(f"You have {chances} chances left.")
                if chances==0:
                    print(f"You ran out of chances. The number was {chosen_number}.")
                    break
            elif ((guess-chosen_number)<=10 and (guess-chosen_number)>0) or ((chosen_number-guess)<=10 and (chosen_number-guess)>0):
                print("Almost close!!!!!!")
                chances-=1
                print(f"You have {chances} chances left.")
                if chances==0:
                    print(f"You ran out of chances. The number was {chosen_number}.")
                    break
            elif (guess-chosen_number)>100 or (chosen_number-guess)>100:
                print("Invalid input. Try again. Your guess should be between 0-100.")
                continue
            else:
                print(f"Congratulations !!!!!\nYou got the right number. The number was {chosen_number}.")
                break
        break
    else:
        print("Invalid difficulty selection. Please try again.")
    continue
print("Thanks for using my program. Bye !!!!")