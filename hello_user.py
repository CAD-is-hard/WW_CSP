# WW, Hello User
while True:
    name = input("What is your first name: ").title().strip()
    if name.isnumeric():
        print("That is a number, not a name")
    elif " " in name:
        print("That's more than one name")
    else:
        print(f"Hello {name}, have a great day!")