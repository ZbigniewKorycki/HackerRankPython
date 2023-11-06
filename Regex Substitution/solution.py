import re

def replace_to_and(match):
    return " and "

def replace_to_or(match):
    return " or "


for _ in range(int(input())):
    line_of_text = input()
    while True:
        matches_and = re.search("\s(&&)\s", line_of_text)
        if matches_and:
            line_of_text = re.sub("\s&&\s", replace_to_and, line_of_text, 1)
        else:
            break
    while True:
        matches_or = re.search("\s(\|\|)\s", line_of_text)
        if matches_or:
            line_of_text = re.sub("\s(\|\|)\s", replace_to_or, line_of_text, 1)
        else:
            break
    print(line_of_text)