import csv,string,random,os
from random import randint

with open(os.path.join("data","all_words.csv")) as f:
    words = [line.rstrip('\n') for line in f]
f.close

def create_text(min_length, max_length):
    output = ""
    new_output = ""

    i = 0
    while i < int(max_length):

        if len(new_output) == 0:
            new_output = random.choice(words)
        else:
            new_output = new_output + " " + random.choice(words)
#        print len(new_output)
#        print max_length

        if len(new_output) < max_length:
            output = new_output
        i = len(new_output)

    return output

print create_text(0,200)
