import csv,string,random,os,faker
from random import randint
from datetime import datetime
from faker import Faker
from datetime import datetime

#Request number of rows from user
test_data_rows = input("How many rows of test data do you need? (Enter an integer, please!) ")

script_start_time = datetime.now()

####### BEGIN FUNTION DECLARATIONS #########

def create_char_fixed(min_length, max_length):
    output = ""
    i = 0
    while i < max_length:
        output = output + random.choice(string.ascii_uppercase+string.ascii_lowercase)
        i = i+1
    return output

def create_char_var(min_length, max_length):
    output = ""
    i = 0
    y = randint(1,max_length)
    while i < y:
        output = output + random.choice(string.ascii_uppercase+string.ascii_lowercase)
        i = i+1
    return output

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

def create_numeric(min_length,max_length):
    output = str(randint(min_length,max_length))
    return output

def nhs_number():
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

def create_nhs_number(allow_invalid):
    if allow_invalid == 1:
        return nhs_number()
    else:
        nhs = nhs_number()
        while nhs == "0":
            nhs = nhs_number()
        return nhs

def create_postcode():
    return fake.postcode()

def create_first_name():
    return first_names[randint(0,len(first_names)-1)]

def create_last_name():
    last_name = ""
    return last_names[randint(0,len(last_names)-1)]

def create_datetime_range(min_date, max_date):
    d1 = datetime.strptime(min_date, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.strptime(max_date, '%Y-%m-%d %H:%M:%S')
    return fake.date_between_dates(date_start=d1, date_end=d2)


def generate_row():
    output_row = ""
    for row in range(len(field_settings)): #For each field specified in the settings file
        min_length = field_settings[row][1]
        max_length = field_settings[row][2]
        field_type = field_settings[row][3]
        percent_completed = int(field_settings[row][4])

        if min_length == "":
            min_length = 0

        if randint(0,100) <= percent_completed:
            #field_type determines how data is generated
            if field_type == "nhs_number":
                output_row = output_row + create_nhs_number(0) + delimiter
            elif field_type == "first_name":
                output_row = output_row + create_first_name() + delimiter
            elif field_type == "last_name":
                output_row = output_row + create_last_name() + delimiter
            elif field_type == "text":
                output_row = output_row + create_text(int(min_length),int(max_length)) + delimiter
            elif field_type == "numeric":
                output_row = output_row + create_numeric(int(min_length),int(max_length)) + delimiter
            elif field_type == "char_fixed":
                output_row = output_row + create_char_fixed(0,int(max_length)) + delimiter
            elif field_type == "char_var":
                output_row = output_row + create_char_var(0,int(max_length)) + delimiter
            elif field_type == "postcode":
                output_row = output_row + create_postcode() + delimiter
            elif field_type == "datetime_range":
                output_row = output_row + str(create_datetime_range(min_length,max_length)) + delimiter
            else:
                output_row = output_row + "INCORRECT FIELD TYPE" + delimiter
        else:
            output_row = output_row + delimiter
        #output row to text file
    output_row = output_row[:-1]
    return output_row

def in_list(item,L): #used to get items from config file, eg config[in_list("config item")][1]
    for i in L:
        if item in i:
            return L.index(i)
    return -1

fake = Faker('en_GB') #used for postcode, address functions and date/times

####### END FUNCTION DECLARATIONS #########

#Load dictionary
with open(os.path.join("data","all_words.csv")) as f:
    words = [line.rstrip('\n') for line in f]
f.close

#Load forenames
with open(os.path.join("data","first_names.csv")) as f:
    first_names = [line.rstrip('\n') for line in f]
f.close

#Load last_names
with open(os.path.join("data","last_names.csv")) as f:
    last_names = [line.rstrip('\n') for line in f]
f.close

#load postcodes
with open(os.path.join("data","postcode.csv")) as f:
    postcodes = [line.rstrip('\n') for line in f]
f.close

#Load config file into a list
f = open('config.csv', 'r')
datareader = csv.reader(f,delimiter=',')
config = []
for row in datareader:
    config.append(row)
f.close

delimiter = config[in_list('delimiter',config)][1]

#Delete header row from config list
del config[0]

#Load field_settings file into a list
settings_file = config[in_list('field_settings_filename',config)][1]

datafile = open(settings_file, 'r')
datareader = csv.reader(datafile,delimiter=',')
field_settings = []
for row in datareader:
    field_settings.append(row)

#Delete header row from field settings list
del field_settings[0]

### Begin main program



#Output all goes in here
output_array = []

#Create header row for output file
header_row = ""
for row in range(len(field_settings)):
    header_row = header_row + field_settings[row][0] + delimiter

output_array.append(header_row[:-1]) #write header row to output list


data_type = ""
max_length = 0
field_type = ""

#print test_data_rows

i = 0
while i < test_data_rows:
    output_array.append(generate_row())
    i = i+1

print "Writing data to output file"

#Output array to text file
output_file = open('output.csv', 'w')

for item in output_array:
  output_file.write("%s\n" % item)

print "Script completed in " + str(datetime.now() - script_start_time)
