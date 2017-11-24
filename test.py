import csv,string,random,os,pyodbc,faker
from random import randint
from faker import Faker

fake = Faker()

#Load config file into a list
f = open('config.csv', 'r')
datareader = csv.reader(f,delimiter=',')
config = []
for row in datareader:
    config.append(row)
f.close

#Delete header row from config list
del config[0]

print config

if "date_format" in config:
    print "yeah!"

print fake.date_time()



def in_list(item,L):
    for i in L:
        if item in i:
            return L.index(i)
    return -1

print config[in_list('delimiter',config)][1]
