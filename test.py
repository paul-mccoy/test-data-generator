from random import randint
import string
import random


def generic(type, length, minval=0, maxval=0):
    if type == "character":
        generic_output = ""
        i = 0
        while i < length:
            generic_output = generic_output + random.choice(string.ascii_uppercase+string.ascii_lowercase)
            i = i+1
        return generic_output
    else:
        generic_output = randint(minval,maxval)
        return generic_output

print generic("character","30",0,3452626)
