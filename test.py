import csv,string,random,os,pyodbc,faker,datetime
from random import randint
from random import randrange
from faker import Faker
from datetime import datetime
from datetime import timedelta



fake = Faker('en_GB')

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

print fake.date_time()



def in_list(item,L):
    for i in L:
        if item in i:
            return L.index(i)
    return -1

print datetime.today()

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


d1 = datetime.strptime('2008-01-01 00:30:01', '%Y-%m-%d %H:%M:%S')
d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')


print random_date(d1, d2)

#print fake.date_between_dates(date_start=d1, date_end=d2)
