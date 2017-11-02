import csv
from random import randint

####### BEGIN FUNTION DECLARATIONS #########

def create_nhs_number():
    #initialise list
    nhs_number = []

    #generate first 9 digits and store each seperately in the list
    for i in range(0,9):
        nhs_number.append(randint(0, 9))

    digit_sum = 0 #stores sum of digits to calculate checksum digit

    #concatentate all 9 digits as a string
    nhs_number_complete = ""
    for i in nhs_number:
        nhs_number_complete = nhs_number_complete + str(i)

    i=0
    while i < 9:
        digit_sum = digit_sum + nhs_number[i] * (10-i)
        i = i+1

    nhs_modulus = digit_sum % 11

    #calculate checksum digit
    check_digit = 11 - nhs_modulus

    if check_digit == 10:
        nhs_number_complete = "0"
        return nhs_number_complete
    elif check_digit == 11:
        nhs_number_complete = nhs_number_complete + str(0)
        return nhs_number_complete
    else:
        nhs_number_complete = nhs_number_complete + str(check_digit)
        return nhs_number_complete

def nhs_number(allow_invalid):
    if allow_invalid == 1:
        return create_nhs_number()
    else:
        nhs = create_nhs_number()
        while nhs == "0":
            nhs = create_nhs_number()
        return nhs

####### END FUNCTION DECLARATIONS #########

#Load dictionary
with open("all_words.csv") as f:
    words = [line.rstrip('\n') for line in f]

#Load settings file into a list
datafile = open('field_settings.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
field_settings = []
for row in datareader:
    field_settings.append(row)

#Delete header row from field settings list
del field_settings[0]

### Begin main program

#Create header row for output file
header_row = ""
for row in range(len(field_settings)):
    header_row = header_row + field_settings[row][0] + ","
header_row = header_row[:-1]
print header_row
