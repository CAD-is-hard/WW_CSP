# WW, Loops Notes
import random
# code that will repeat over and over again
count = 1

while count <= 10:
    print(count)
    count += 1


goose = random.randint(1,11)
ducks = 1

while True:
    print("duck")
    if ducks == goose:
        break
    ducks += 1
print("GOOSE!!!")


siblings = ["Ela", "Eliza", "Thomas", "James", "Richard"]
print(siblings[2])
print(siblings)
item = input("What needs to be added to the list: ")
siblings.append(item)
siblings.insert(4, "William")
print(siblings)
siblings.pop(1)
print(siblings)

# For loops
for number in range(1, 11):
    print(number)

for sibling in siblings:
    print(sibling + " Wilcox")