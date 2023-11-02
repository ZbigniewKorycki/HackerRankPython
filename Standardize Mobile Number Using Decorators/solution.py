def wrapper(f):
    def fun(l):
        new_list = []
        for number in l:
            if len(number) == 10:
                new_list.append('+91' + ' ' + number[0:5] + ' ' + number[5:10])
            elif len(number) == 11 and number[0] == '0':
                new_number = number[1:]
                new_list.append('+91' + ' '+ new_number[0:5] + ' ' + new_number[5:10])
            elif len(number) == 12 and number[:2] == '91':
                new_number = number[2:]
                new_list.append('+91' + ' '+ new_number[0:5] + ' ' + new_number[5:10])
            elif len(number) == 13 and number[:3] == '+91':
                new_number = number[3:]
                new_list.append('+91' + ' ' + new_number[0:5] + ' ' + new_number[5:10])
        return f(new_list)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)