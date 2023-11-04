import re

n_cases = int(input())

for _ in range(n_cases):
    card_number = input()
    match = re.search('^[456]\d{3}(\-?\d{4}){3}$', card_number)
    if match:
        card_numbers_without_hyphens = card_number.replace("-", "")
        match_without_hyphens = re.search(r'(\d)\1\1\1', card_numbers_without_hyphens)
        if match_without_hyphens:
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")