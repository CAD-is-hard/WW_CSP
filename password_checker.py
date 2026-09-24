# WW - Password Strength Checker

password = input("What is your password: ").strip()

length = len(password)

has_upper = False
has_lower = False
has_number = False
has_symbol = False

for letter in password:
    if letter.isupper():
        has_upper = True

    if letter.islower():
        has_lower = True

    if letter.isnumeric():
        has_number = True

symbols = "!@#$%^&*"

for letter in password:
    if letter in symbols:
        has_symbol = True

has_length = length >= 8

print()
print(f"At least 8 characters: {has_length}")
print(f"Has an uppercase letter: {has_upper}")
print(f"Has a lowercase letter: {has_lower}")
print(f"Has a number: {has_number}")
print(f"Has a symbol: {has_symbol}")

rules_met = 0

if has_length:
    rules_met += 1

if has_upper:
    rules_met += 1

if has_lower:
    rules_met += 1

if has_number:
    rules_met += 1

if has_symbol:
    rules_met += 1

if rules_met == 5:
    strength = "Strong"
elif rules_met >= 3:
    strength = "Medium"
else:
    strength = "Weak"

print()
print(f"Your password strength is: {strength}")

if strength != "Strong":
    print("To make it Strong, add:")

    if not has_length:
        print("- At least 8 characters")

    if not has_upper:
        print("- An uppercase letter")

    if not has_lower:
        print("- A lowercase letter")

    if not has_number:
        print("- A number")

    if not has_symbol:
        print("- A symbol")