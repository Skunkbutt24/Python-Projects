from art import logo
print(logo)
print("Welcome to my Caesar Cipher program. Here you can encode or decode your message. Let's get started.")
import string
charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for char in original_text:
        if char in charset:
            shifted_position = charset.index(char) + shift_amount
            shifted_position %= len(charset)
            cipher_text += charset[shifted_position]
        else:
            cipher_text += char
    print(f"Here is the encoded result: {cipher_text}")
def decrypt(cipher_text, shift_amount):
    original_text = ""
    for char in cipher_text:
        if char in charset:
            shifted_position = charset.index(char) - shift_amount
            shifted_position %= len(charset)
            original_text += charset[shifted_position]
        else:
            original_text += char
    print(f"Here is the decoded result: {original_text}")
while True:
    direction = input('Type "Encode" to encrypt, Type "Decode" to decrypt:\n').lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    shift %= len(charset)
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid input for direction. Please type 'encode' or 'decode'.")
    start_over = input("Do you want to start over? Type Yes or No:\n").lower()
    if start_over != "yes":
        print("Goodbye!!!!")
        break
