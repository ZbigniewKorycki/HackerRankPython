def check_if_valid_uid(uid):
    counter_upper_letters = 0
    counter_numbers = 0
    for symbol in uid:
        if symbol.isdigit():
            counter_numbers += 1
        elif symbol.isupper():
            counter_upper_letters += 1
    num_of_distinct_characters = len(set(uid))
    if (uid.isalnum()) and (num_of_distinct_characters == 10) and (len(uid) == 10) and (counter_upper_letters >= 2) and (counter_numbers >= 3):
        print("Valid")
    else:
        print("Invalid")


for iteration in range(int(input())):
    check_if_valid_uid(input())