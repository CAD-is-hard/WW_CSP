# WW, Password Checker
password = input("What is your password: ").strip()

length = int(len(password))

has_upper = "False"

has_lower = "False"

has_number = "False"

has_symbol = int("False")

count = "0"

for letter in password:
    if letter.isupper:
        has_upper = "True"
    else:
        has_upper = "False"
    if letter.islower:
        has_lower = "True"
    else:
        has_lower = "False"
    if letter.isnumeric:
        has_number = "True"
    else:
        has_number = "False"
if length = "True"

if "!@#$%^&*" in password:
    has_symbol = "True"
else:
    has_symbol = "False"

if length >= 8:
    print(f"At least 8 characters: True")
else:
    print(f"At least 8 characters: False")
print(f"Has an uppercase letter: {has_upper}")
print(f"Has an lowercase letter: {has_lower}")
print(f"Has a number: {has_number}")