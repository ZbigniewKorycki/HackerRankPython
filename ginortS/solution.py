lower_letters = []
upper_letters = []
even_digits = []
odd_digits = []

def sort_string(string):
    for element in string:
        if element.isalpha():
            if element.isupper():
                upper_letters.append(element)
            else:
                lower_letters.append(element)
        elif element.isdigit():
            if int(element) % 2 != 0:
                odd_digits.append(element)
            else:
                even_digits.append(element)


string_to_format = list(input())
sort_string(string_to_format)
lower_letters.sort()
upper_letters.sort()
even_digits.sort()
odd_digits.sort()

print(''.join(lower_letters + upper_letters + odd_digits + even_digits))