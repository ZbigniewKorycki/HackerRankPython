while True:
    vertical, horizontal = map(int, input().split())
    if (5 < vertical < 101) and (vertical % 2 == 1) and (horizontal / 3 == vertical):
        break

mat_symbols = '.|.'
extreme_line = mat_symbols[0].rjust(int((horizontal - 1) / 2), '-') + "|" + mat_symbols[0].ljust(
    int((horizontal - 1) / 2), '-')

half_vertical = int((vertical - 1) / 2)

for x in range(int((vertical - 1) / 2)):
    if x == 0:
        print(extreme_line)
    else:
        left_side_symbols = mat_symbols * x + mat_symbols[0]
        right_side_symbols = mat_symbols[0] + mat_symbols * x
        print(
            left_side_symbols.rjust(int((horizontal - 1) / 2), '-') + "|" + right_side_symbols.ljust(
                int((horizontal - 1) / 2), '-'))

print("WELCOME".center(horizontal, '-'))

for x in range(int((vertical - 1) / 2) - 1, -1, -1):
    if x == 0:
        print(extreme_line)
    else:
        left_side_symbols = mat_symbols * x + mat_symbols[0]
        right_side_symbols = mat_symbols[0] + mat_symbols * x
        print(
            left_side_symbols.rjust(int((horizontal - 1) / 2), '-') + "|" + right_side_symbols.ljust(
                int((horizontal - 1) / 2), '-'))
