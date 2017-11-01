
import csv
datafile = open('field_settings.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
data = []
for row in datareader:
    data.append(row)

print(data)
