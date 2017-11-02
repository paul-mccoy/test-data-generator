from random import randint

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
        print "invalid not allowed"
        nhs = create_nhs_number()
        while nhs == "0":
            nhs = create_nhs_number()
        return nhs

for i in range(100):
    print nhs_number(0)
