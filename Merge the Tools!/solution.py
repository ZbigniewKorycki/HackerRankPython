def merge_the_tools(string, k):
    new_list = []
    working_string = []
    counter = 0
    for letter in string:
        if letter in working_string:
            counter += 1
        else:
            working_string.append(letter)
            counter += 1
        if counter == k:
            released_string = ''.join(working_string)
            new_list.append(released_string)
            working_string.clear()
            counter = 0

    [print(''.join(string_mini_list)) for string_mini_list in new_list]


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)