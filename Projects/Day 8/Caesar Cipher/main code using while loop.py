from art import logo
print(logo)
import string
charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
def encrypt(original_text, shift_amount):
    cipher_text = ""
    index = 0
    while index < len(original_text):
        char = original_text[index]
        if char in charset:
            shifted_position = charset.index(char) + shift_amount
            shifted_position %= len(charset)
            cipher_text += charset[shifted_position]
        else:
            cipher_text += char
        index += 1
    print(f"Here is the encoded result: {cipher_text}")
def decrypt(cipher_text, shift_amount):
    original_text = ""
    index = 0
    while index < len(cipher_text):
        char = cipher_text[index]
        if char in charset:
            shifted_position = charset.index(char) - shift_amount
            shifted_position %= len(charset)
            original_text += charset[shifted_position]
        else:
            original_text += char
        index += 1
    print(f"Here is the decoded result: {original_text}")
while True:
    direction = input('Type "Encode" to encrypt, Type "Decode" to decrypt:\n').lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    shift %= len(charset)
    if direction == "encode":
        encrypt(text, shift)
        continue_prompt = input("Do you want to decode now? Type Yes or No:\n").lower()
        if continue_prompt == "yes":
            text_to_decode = input("Type the encoded message:\n")
            decrypt(text_to_decode, shift)
    elif direction == "decode":
        decrypt(text, shift)
        continue_prompt = input("Do you want to encode now? Type Yes or No:\n").lower()
        if continue_prompt == "yes":
            text_to_encode = input("Type the message to encode:\n")
            encrypt(text_to_encode, shift)
    else:
        print("Invalid input for direction. Please type 'encode' or 'decode'.")
    start_over = input("Do you want to start over? Type Yes or No:\n").lower()
    if start_over != "yes":
        print("Goodbye!")
        break
