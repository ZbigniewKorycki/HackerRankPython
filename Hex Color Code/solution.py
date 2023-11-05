import re

for _ in range(int(input())):
    line_of_code = input()
    matches = re.findall('(?!^#)#[\da-fA-F]{3,6}', line_of_code)
    if matches:
        for match in matches:
            print(match)
