logo = """
_____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid Operation."
def calculator():
    while True:
        num1 = float(input("Enter a number: "))
        while True:
            operation = input("Pick an operation (+, -, *, /): ")
            num2 = float(input("Enter next number: "))
            result = calculate(num1, num2, operation)
            if result == "Invalid Operation.":
                print(result)
                retry = input("Invalid Operation. Do you want to retry? (yes/no)\n").lower()
                if retry != "yes":
                    print("Good Bye !!!!!\nThank you for using my program.")
                    break
            else:
                print(f"{num1} {operation} {num2} = {result}")
                num1 = result
            continue_program = input("Do you want to continue? (yes/no)\n").lower()
            if continue_program != "yes":
                print("Good Bye !!!!!\nThank you for using my program.")
                break
calculator()
