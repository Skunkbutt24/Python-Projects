import math
print("Welcome to paint calculator program. Let's get started.\n")
def paint_calc(height, width, cover):
  num_cans = (height * width) / cover
  round_up_cans = math.ceil(num_cans)
  print(f"You'll need {round_up_cans} cans of paint.")
test_h = int(input("What would be the height of wall: ")) 
test_w = int(input("What would be the width of wall: ")) 
coverage = int(input("How much area can you paint with one can : "))
paint_calc(height=test_h, width=test_w, cover=coverage)