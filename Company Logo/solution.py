from collections import Counter

def sort_letter_by_occurrence_and_position(element):
    return element[1], 1/ord(element[0])


if __name__ == '__main__':
    s = input().lower()
    x = Counter(s)
    x_dict = dict(x)
    sort_x = sorted(x_dict.items(), key=sort_letter_by_occurrence_and_position, reverse=True)
    for letter, occurrence in sort_x[0:3]:
        print(letter, occurrence)
