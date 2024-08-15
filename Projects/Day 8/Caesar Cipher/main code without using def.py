from art import logo
print(logo)
print("Welcome to my Caesar Cipher program. Here you can encode or decode your message. Let's get started.")
import string
charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
while True:
    encode_decode = input('Type "Encode" to encrypt, Type "Decode" to decrypt:\n').lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    shift %= len(charset)
    if encode_decode == "encode":
        cipher_text = ""
        for char in text:
            if char in charset:
                shifted_position = charset.index(char) + shift
                shifted_position %= len(charset)
                cipher_text += charset[shifted_position]
            else:
                cipher_text += char
        print(f"Here is the encoded result: {cipher_text}")
    elif encode_decode == "decode":
        original_text = ""
        for char in text:
            if char in charset:
                shifted_position = charset.index(char) - shift
                shifted_position %= len(charset)
                original_text += charset[shifted_position]
            else:
                original_text += char
        print(f"Here is the decoded result: {original_text}")
    else:
        retry=input(("Invalid input for direction. Do you want to retry ?\n")).lower()
        if retry!="yes":
            print("Good bye !!!")
            break
        else:
            continue
    start_over = input("Do you want to start over? Type Yes or No:\n").lower()
    if start_over != "yes":
        print("Goodbye!!!!")
        break
