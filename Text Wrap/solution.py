import textwrap


def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.fill(text=string)
    return word_list


if __name__ == '__main__':
    string, max_width = input("String: "), int(input("Max width: "))
    result = wrap(string, max_width)
    print(result)

