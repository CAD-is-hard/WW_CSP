# WW, Fixing Inputs

# When you want a specific input
while True:
    color = input("Tell me a color that is only one word: ").lower().strip()
    if color.isnumeric():
        print("Sorry that is a number")
    elif " " in color:
        print("I said one word")
    else:
       print(f"I painted your walls {color}!")
