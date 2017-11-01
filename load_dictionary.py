#delete this bit later
from random import randint

with open("all_words.csv") as f:
    lines = [line.rstrip('\n') for line in f]

print lines[randint(0,len(lines))]
