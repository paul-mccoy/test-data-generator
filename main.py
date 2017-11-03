import csv,string,random,os
from random import randint

####### BEGIN FUNTION DECLARATIONS #########

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

def forename():
    forename = ""
    return forenames[randint(0,len(forenames))]

def last_name():
    last_name = ""
    return last_names[randint(0,len(last_names))]

def generate_row():
    output_row = ""
    for row in range(len(field_settings)):
        data_type = field_settings[row][1]
        field_length = field_settings[row][2]
        field_type = field_settings[row][3]

        if field_length == "":
            field_length = 0

        #field_type determines how data is generated
        if field_type == "nhs_number":
            output_row = output_row + nhs_number(0) + ","
        elif field_type == "forename":
            output_row = output_row + forename() + ","
        elif field_type == "last_name":
            output_row = output_row + last_name() + ","
        else: #generic field
            output_row = output_row + str(generic(data_type,int(field_length),0,65000))+","

        #output row to text file
    output_row = output_row[:-1]
    return output_row

####### END FUNCTION DECLARATIONS #########

#Load dictionary
with open(os.path.join("data","all_words.csv")) as f:
    words = [line.rstrip('\n') for line in f]
f.close

#Load forenames
with open(os.path.join("data","first_names.csv")) as f:
    forenames = [line.rstrip('\n') for line in f]
f.close

#Load last_names
with open(os.path.join("data","last_names.csv")) as f:
    last_names = [line.rstrip('\n') for line in f]
f.close

#Load settings file into a list
datafile = open('field_settings.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
field_settings = []
for row in datareader:
    field_settings.append(row)

#Delete header row from field settings list
del field_settings[0]

### Begin main program

#Request number of rows from user
test_data_rows = input("How many rows of test data do you need? (Enter an integer, please!) ")

#Output all goes in here
output_array = []

#Create header row for output file
header_row = ""
for row in range(len(field_settings)):
    header_row = header_row + field_settings[row][0] + ","

output_array.append(header_row[:-1]) #write header row to output list


data_type = ""
field_length = 0
field_type = ""

#print test_data_rows

i = 0
while i < test_data_rows:
    output_array.append(generate_row())
    i = i+1

#Output array to text file
output_file = open('output.csv', 'w')

for item in output_array:
  output_file.write("%s\n" % item)
