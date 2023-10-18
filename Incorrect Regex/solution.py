import re

def if_regex_valid(string):
    try:
        re.compile(string)
    except re.error:
        print("False")
    else:
        print("True")

if __name__ == "__main__":
    for _ in range(int(input())):
        regex_string = input()
        if_regex_valid(regex_string)

