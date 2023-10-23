import re

def check_if_phone_number_is_valid(string):
    x = re.search(r"^[789][^A-Za-z]*$", string)
    if x and len(string) == 10:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    num_of_inputs = int(input())
    for _ in range(num_of_inputs):
        check_if_phone_number_is_valid(input())

