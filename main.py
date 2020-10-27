# This is a simple program python that reads a text file,
# and then reads one line of the Text File inside, then prints the text.
# By Febhost32
import random

print("Hello! \nType g to get words from .txt file \ntype a to add new words to .txt file. \n \n")

file = open("words.txt", "r+")
words = []
selection = "g"

for line in file:
    words.append(line.strip())


selection = input("Selection (g/a/s)? ")
print("\n")

while selection != "s":
    if selection == "g":
        randomnumber = random.randint(0, len(words) - 1)
        print(words[randomnumber])
        print("\n")
        selection = input("Selection (g/a/s)? ")
        print("\n")
    elif selection == "a":
        print("Insert your words here : ")
        add = "\n" + input()
        file.write(add)
        print("Words added! \n")
        selection = input("Selection (g/a/s)? ")
        print("\n")
    else :
        file.close



