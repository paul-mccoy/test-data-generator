import random,os,string
from random import randint

#Load forenames
with open(os.path.join("data","first_names.csv")) as f:
    forenames = [line.rstrip('\n') for line in f]
f.close

print forenames[3]

def forename():
    forename = ""
    return forenames[randint(0,len(forenames))]

print forename()
