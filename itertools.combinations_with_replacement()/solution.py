from itertools import combinations_with_replacement

string, size = input().split()
combinations = [print(''.join(comb)) for comb in list(combinations_with_replacement(sorted(string), int(size)))]
