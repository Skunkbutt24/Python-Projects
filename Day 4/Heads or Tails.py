print("Welcome, to my virtual Heads or Tail program. Let's get started")
user_input=input("Do you want to use my program ?\nPress Enter to start. ")
if user_input=="":
    import random
    generate=random.randint(0,1)
    if generate==0:
        print("You got Heads")
    else:
        print("You got tails")
    print("Thanks for using my program.")
else:
    print("No worries. Bye, take care.")