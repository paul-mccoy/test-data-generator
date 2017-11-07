import csv,string,random,os,pyodbc
from random import randint

with open(os.path.join("data","postcode.csv")) as f:
    postcodes = [line.rstrip('\n') for line in f]
f.close

def create_postcode():
    return random.choice(postcodes)

print create_postcode()
