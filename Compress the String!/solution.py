from itertools import groupby

for num, group in groupby(input()):
    print(f"({len(list(group))}, {num})", end=" ")

