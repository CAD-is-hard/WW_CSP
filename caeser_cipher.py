# WW, Caeser Cipher
direction = input("Do you want to (E)ncode or (D)ecode: ")
message = input("What is your message: ").strip()
amount = input("How much do you want to shift: ")
for letter in message:
    if letter.isnumeric:
        
        print(letter)
def caeser_shift(message, shift):
    return message + shift
print(f"your shifted message is {message,amount}")
