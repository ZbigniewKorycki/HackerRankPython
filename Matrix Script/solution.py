import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix_lines_as_list = [list(line) for line in matrix]

matrix_sorted_by_character_position = []

for _ in range(m):
    for line in matrix_lines_as_list:
        first_item = line.pop(0)
        matrix_sorted_by_character_position.append(first_item)

matrix_sorted_by_character_position_as_string = ''.join(matrix_sorted_by_character_position)

match = re.sub('(?<=[a-zA-Z0-9])[!@#$%& ]+(?=[a-zA-Z0-9])', ' ', matrix_sorted_by_character_position_as_string)

print(match)




