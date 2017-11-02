from random import randint

#initialise list
nhs_number = []

#generate first 9 digits and store each seperately in the list
for i in range(0,9):
    nhs_number.append(randint(0, 9))

digit_sum = 0

nhs_number_complete = ""
for i in nhs_number:
    nhs_number_complete = nhs_number_complete + str(i)

i=0
while i < 9:
    digit_sum = digit_sum + nhs_number[i] * (10-i)
    i = i+1
nhs_modulus = digit_sum % 11
print nhs_modulus
check_digit = 11 - nhs_modulus

if check_digit == 10:
    print 0
elif check_digit == 11:
    nhs_number_complete = nhs_number_complete + str(0)
    print nhs_number_complete
else:
    nhs_number_complete = nhs_number_complete + str(check_digit)
    print nhs_number_complete
