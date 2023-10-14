def is_float(string):
    try:
        float(string)
    except:
        return False
    else:
        if (string[0] in ['+', '-', '.'] or string[0].isdecimal()) and (string.count(".") == 1) \
                and (string.split('.')[1].isnumeric()):
            return True
        else:
            return False


for _ in range(int(input())):
    print(is_float(input()))