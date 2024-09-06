import string
print("Welcome to the Alphabet Frequency Counter!")
print("Enter a passage, and the program will count the occurrences of each letter (A-Z).")
passage = input("Please enter a passage:\n ")
letters=string.ascii_uppercase
char_counts = {}
for char in letters:
    char_counts[char] = 0
upper_passage=passage.upper()
for char in passage:
    if char in char_counts:
        char_counts[char] += 1
print("Character Frequency Count:")
for char in letters:
    print(f"{char} = {char_counts[char]}")
uppercase=0
lowercase=0
numbers=0
symbols=0
for char in passage:
    if char.isupper():
        uppercase+=1
    elif char.islower():
        lowercase+=1
    elif char.isdigit():
        numbers+=1
    else:
        symbols+=1
print(f"Total Uppercase: {uppercase}")
print(f"Total Lowercase: {lowercase}")
print(f"Total Numbers: {numbers}")
print(f"Total Symbols: {symbols}")