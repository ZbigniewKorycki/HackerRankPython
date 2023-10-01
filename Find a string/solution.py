def count_substring(string, sub_string):
    occurrence_of_substring = set()

    for i in range(0, len(string)):
        count_sub = string.find(sub_string, i)
        if count_sub >= 0:
            occurrence_of_substring.add(count_sub)

    return len(occurrence_of_substring)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)