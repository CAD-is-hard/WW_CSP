# WW, Reading and Writing to Files

with open('practice.txt', "r+") as file:
    content = file.read()
    print(content)
    word = content.find("Wilcox")
    length = len("Wilcox")
    content += " Thomas!"
    file.write(content)

with open('practice.txt',"w") as file:
    file.write("Hello")