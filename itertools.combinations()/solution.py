from itertools import combinations


def print_combinations_up_to_size():
    string, size = input().split()
    for x in range(1, int(size) + 1):
        combinations_for_size_x = list(combinations(sorted(string), x))
        for comb in combinations_for_size_x:
            print("".join(list(comb)))


print_combinations_up_to_size()

