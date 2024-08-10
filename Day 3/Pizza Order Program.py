print("Good Morning, Sir")
small_pizza=15
medium_pizza=20
large_pizza=25
small_pizza_pepperoni=2
medium_large_pizza_pepperoni=3
extra_cheese=1
size=input("What would be your pizza size ? :")
pepperoni=input("Do you want to add pepperoni ? :")
cheese=input("Do you want to add extra cheese ? :")
if (size=="S" and pepperoni=="Y" and cheese =="Y"):
    bill=small_pizza+small_pizza_pepperoni+extra_cheese
    print(f"Thank you for choosing Python Pizza Deliveries!\n Your final bill is : ${bill}")
elif (size=="S" and pepperoni=="N" and cheese =="Y"):
    bill=small_pizza+extra_cheese
    print(f"Thank you for choosing Python Pizza Deliveries!\n Your final bill is : ${bill}")
elif (size=="S" and pepperoni=="Y" and cheese =="N"):
    bill=small_pizza+small_pizza_pepperoni
    print(f"Thank you for choosing Python Pizza Deliveries!\n Your final bill is : ${bill}")
elif (size=="S" and pepperoni=="N" and cheese =="N"):
    bill=small_pizza
    print(f"Thank you for choosing Python Pizza Deliveries!\n Your final bill is : ${bill}")
if (size=="M" and pepperoni=="Y" and cheese =="Y"):
    bill=medium_pizza+medium_large_pizza_pepperoni+extra_cheese
    print(f"Thank you for choosing Python Pizza Deliveries!\n Your final bill is : ${bill}")
elif (size=="M" and pepperoni=="Y" and cheese =="N"):
    bill=medium_pizza+medium_large_pizza_pepperoni
    print(f"Thank you for choosing Python Pizza Deliveries!\n Your final bill is : ${bill}")
elif (size=="M" and pepperoni=="N" and cheese =="Y"):
    bill=medium_pizza+extra_cheese
    print(f"Thank you for choosing Python Pizza Deliveries!\n Your final bill is : ${bill}")
elif (size=="M" and pepperoni=="N" and cheese =="N"):
    bill=medium_pizza
    print(f"Thank you for choosing Python Pizza Deliveries!\n Your final bill is : ${bill}")
if (size=="L" and pepperoni=="Y" and cheese =="Y"):
    bill=large_pizza+medium_large_pizza_pepperoni+extra_cheese
    print(f"Thank you for choosing Python Pizza Deliveries!\n Your final bill is : ${bill}")
elif (size=="L" and pepperoni=="Y" and cheese =="N"):
    bill=large_pizza+medium_large_pizza_pepperoni
    print(f"Thank you for choosing Python Pizza Deliveries!\n Your final bill is : ${bill}")
elif (size=="L" and pepperoni=="N" and cheese =="Y"):
    bill=large_pizza+extra_cheese
    print(f"Thank you for choosing Python Pizza Deliveries!\n Your final bill is : ${bill}")
elif (size=="L" and pepperoni=="N" and cheese =="N"):
    bill=large_pizza
    print(f"Thank you for choosing Python Pizza Deliveries!\n Your final bill is : ${bill}")
   