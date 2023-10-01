if __name__ == '__main__':
    s = input()

    alphanum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for char in s:
        if char.isalnum():
            alphanum = True
        if char.isalpha():
            alpha = True
        if char.isdigit():
            digit = True
        if char.islower():
            lower = True
        if char.isupper():
            upper = True

    print(alphanum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)