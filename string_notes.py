# WW, String Notes
first_name = 'William'
last_name = 'Wilcox'
# concatenation => add two string together
name = first_name + " " + last_name
# escape character lets program ignore next character only works inside of a string
print(f'{name} told the class "You can\'t drive my car"')

user = input("Please tell me your name\n: ").strip().title()

print(f"New user recognized\nWelcome {user}")

# methods

sentence = "The quick brown fox jumped over the lazy dog"
print(f"The sentence is {len(sentence)} characters long")
print(sentence)
print(sentence.replace("dog", name))