# This is a simple program python that reads a text file,
# and then reads one line of the Text File inside, then prints the text.
# By Febhost32
import random

print("Hello! \nType g to get words from .txt file \ntype a to add new words to .txt file. \n \n")

file = open("words.txt", "r+")
words = []
status = ""

for line in file:
    words.append(line.strip())


randomnumber = random.randint(0, len(words)-1)
print(words[randomnumber])



file.close



