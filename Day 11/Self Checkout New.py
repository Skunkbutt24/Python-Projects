logo = """
 .----------------.  .----------------.  .----------------.  .----------------.                                                                                 
| .--------------. || .--------------. || .--------------. || .--------------. |                                                                                
| |    _______   | || |  _________   | || |   _____      | || |  _________   | |                                                                                
| |   /  ___  |  | || | |_   ___  |  | || |  |_   _|     | || | |_   ___  |  | |                                                                                
| |  |  (__ \_|  | || |   | |_  \_|  | || |    | |       | || |   | |_  \_|  | |                                                                                
| |   '.___`-.   | || |   |  _|  _   | || |    | |   _   | || |   |  _|      | |                                                                                
| |  |`\____) |  | || |  _| |___/ |  | || |   _| |__/ |  | || |  _| |_       | |                                                                                
| |  |_______.'  | || | |_________|  | || |  |________|  | || | |_____|      | |                                                                                
| |              | || |              | || |              | || |              | |                                                                                
| '--------------' || '--------------' || '--------------' || '--------------' |                                                                                
 '----------------'  '----------------'  '----------------'  '----------------'                                                                                 
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |  ____  ____  | || |  _________   | || |     ______   | || |  ___  ____   | || |     ____     | || | _____  _____ | || |  _________   | |
| |   .' ___  |  | || | |_   ||   _| | || | |_   ___  |  | || |   .' ___  |  | || | |_  ||_  _|  | || |   .'    `.   | || ||_   _||_   _|| || | |  _   _  |  | |
| |  / .'   \_|  | || |   | |__| |   | || |   | |_  \_|  | || |  / .'   \_|  | || |   | |_/ /    | || |  /  .--.  \  | || |  | |    | |  | || | |_/ | | \_|  | |
| |  | |         | || |   |  __  |   | || |   |  _|  _   | || |  | |         | || |   |  __'.    | || |  | |    | |  | || |  | '    ' |  | || |     | |      | |
| |  \ `.___.'\  | || |  _| |  | |_  | || |  _| |___/ |  | || |  \ `.___.'\  | || |  _| |  \ \_  | || |  \  `--'  /  | || |   \ `--' /   | || |    _| |_     | |
| |   `._____.'  | || | |____||____| | || | |_________|  | || |   `._____.'  | || | |____||____| | || |   `.____.'   | || |    `.__.'    | || |   |_____|    | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'                                                                                
"""
menu = {
    1: {  # Drinks
        "name": "Drinks",
        "items": {
            1: {"Coffee": 2.50},
            2: {"Latte": 3.75},
            3: {"Cappuccino": 3.50},
            4: {"Espresso": 2.00},
            5: {"Sprite": 1.50},
            6: {"Pepsi": 1.50},
            7: {"Milkshake": 5.00},
            8: {"Tea": 2.00},
            9: {"Hot Chocolate": 3.00},
            10: {"Lemonade": 2.50},
            11: {"Orange Juice": 2.75},
            12: {"Iced Coffee": 3.00}
        }
    },
    2: {  # Sandwiches
        "name": "Sandwiches",
        "items": {
            1: {"Grilled Cheese": 6.00},
            2: {"Turkey Club": 8.00},
            3: {"Veggie": 6.50},
            4: {"Ham and Cheese": 7.00},
            5: {"Chicken Caesar": 7.50},
            6: {"BLT": 7.00},
            7: {"Tuna Salad": 7.00},
            8: {"Roast Beef": 8.00},
            9: {"Egg Salad": 6.50},
            10: {"Pastrami": 8.50},
            11: {"BBQ Chicken": 7.50},
            12: {"Falafel": 6.50}
        }
    },
    3: {  # Ice Cream
        "name": "Ice Cream",
        "items": {
            1: {"Vanilla Ice Cream": 3.00},
            2: {"Chocolate Ice Cream": 3.50},
            3: {"Strawberry Ice Cream": 3.00},
            4: {"Mint Chocolate Chip Ice Cream": 3.50},
            5: {"Cookies and Cream Ice Cream": 3.75},
            6: {"Butter Pecan Ice Cream": 3.75},
            7: {"Pistachio Ice Cream": 3.75}
        }
    },
    4: {  # Popcorn
        "name": "Popcorn",
        "items": {
            1: {"Butter Popcorn": 4.00},
            2: {"Cheese Popcorn": 4.50},
            3: {"Caramel Popcorn": 4.50},
            4: {"Kettle Corn Popcorn": 4.50},
            5: {"Spicy Popcorn": 4.00},
            6: {"Garlic Parmesan Popcorn": 4.50},
            7: {"Sour Cream and Onion Popcorn": 4.50}
        }
    },
    5: {  # Milkshakes
        "name": "Milkshakes",
        "items": {
            1: {"Chocolate Milkshake": 5.00},
            2: {"Vanilla Milkshake": 5.00},
            3: {"Strawberry Milkshake": 5.00},
            4: {"Oreo Milkshake": 5.50},
            5: {"Banana Milkshake": 5.00},
            6: {"Peanut Butter Milkshake": 5.50},
            7: {"Mango Milkshake": 5.50}
        }
    },
    6: {  # Pastries
        "name": "Pastries",
        "items": {
            1: {"Croissant": 2.50},
            2: {"Danish": 3.00},
            3: {"Muffin": 2.75},
            4: {"Cinnamon Roll": 3.50},
            5: {"Bagel": 2.00},
            6: {"Scone": 2.75}
        }
    },
    7: {  # Salads
        "name": "Salads",
        "items": {
            1: {"Caesar Salad": 5.00},
            2: {"Greek Salad": 5.50},
            3: {"Garden Salad": 4.50},
            4: {"Chicken Salad": 6.00},
            5: {"Tuna Salad": 6.50}
        }
    }
}
print(logo)
name=input("What's your name ?\n").lower()
print(f"Hi, Mr. {name.capitalize()} !!!!!!\nWelcome to self checkout program. Let's get started.......")
selected_items=[]
selected_items_prices=[]
total_cost=0
start=input("Do you want to start using the program ?\n").lower()
if start=="yes":
    while True:
        print("\n"*50)
        print("====================================================")
        print("\n")
        print("Here are the categories: ")
        for category_number,category_info in menu.items():
            print(f"{category_number}. {category_info["name"]}")
        selected_category_number=int(input("Which category do you want to choose ?\n"))
        category_name=menu[selected_category_number]["name"]
        items=menu[selected_category_number]["items"]
        if selected_category_number not in menu:
            print("Invalid Category selection. Please try again....")
            continue
        while True:
            print("\n"*50)
            print("====================================================")
            print("\n")
            print(f"Here is the menu for {category_name}")
            for item_number,item_info in items.items():
                (item_name,item_price),=item_info.items()
                print(f"{item_number}. {item_name} = {item_price:.2f}$")
            selected_item_number=int(input("Which item do you want to buy ?\n"))
            (item_name,item_price),=items[selected_item_number].items()
            if selected_item_number not in items:
                print("Invalid item selection. Try again......")
                continue
            print("\n"*50)
            print("====================================================")
            print("\n")
            print(f"{item_name} has been added to your cart for {item_price:.2f}$")
            selected_items.append(item_name)
            selected_items_prices.append(item_price)
            print("\n"*50)
            add_items=input("Do you want to add more items from this category ?\n").lower()
            if add_items!="yes":
                break
        print("\n"*50)
        add_category=input("Do you want to choose items from other category ?\n").lower()
        if add_category!="yes":
            break
print("\n"*50)
print("====================================================")
print("\n")
print("Thanks for your order.\nHere is your order summary:\n")
n=1
for item_name,item_price in zip(selected_items,selected_items_prices):
    print(f"{n}. {item_name}: ${item_price:.2f}")
    n+=1
    total_cost += item_price
print(f"================================\nTotal Price: {total_cost:.2f}$")
payment_method = input("How would you like to pay? (Cash 💸, Card 💳, or Mobile 📱)\n").lower()
while payment_method not in ["cash", "card", "mobile"]:
    print("Invalid payment method. Please pay with 'Cash', 'Card', or 'Mobile'.")
    payment_method = input("How would you like to pay? (Cash 💸, Card 💳, or Mobile 📱)\n").lower()
print(f"Payment of ${total_cost:.2f} received via {payment_method}.")
print("Thank you for your purchase!\nSee you again!\nGoodbye...")
        
    
