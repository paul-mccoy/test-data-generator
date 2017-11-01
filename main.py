import csv

#Load dictionary
with open("all_words.csv") as f:
    lines = [line.rstrip('\n') for line in f]

#Load settings file into a list
datafile = open('field_settings.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
field_settings = []
for row in datareader:
    field_settings.append(row)

#Delete header row from field settings list
del field_settings[0]
