# WW, Hangman
import random
with open("words.txt", "r") as file:
    inside = file.readlines()
word = random.choice(inside).strip()

with open("stats.txt", "r") as stats:
    content = stats.read()
    content = content.splitlines()
wins = int(content[0])
losses = int(content[1])
wrong_guesses = 0
print("Welcome to Hangman!")
for letter in word:
    print("_", )\




"""
_______
|     |
|     0
|    /|\\
|    / \\
|_______"""
