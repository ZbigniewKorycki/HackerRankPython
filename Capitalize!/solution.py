# Complete the solve function below.
def solve(s):
    new_string = s.replace(" ", "*")
    fragments = new_string.split("*")
    words = []
    for element in fragments:
        if element == "":
            words.append(element)
        elif element[0].isalpha():
            words.append(element.capitalize())
        else:
            words.append(element)
    return ' '.join(words)
