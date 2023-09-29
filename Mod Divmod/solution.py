a = int(input())
b = int(input())


def divmode_operation(a, b):
    print(divmod(a, b)[0])
    print(divmod(a, b)[1])
    print(divmod(a, b))


divmode_operation(a, b)