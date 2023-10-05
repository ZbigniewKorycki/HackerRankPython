set_N_length = int(input())
set_N = set(list(map(int, input().split()))[0:set_N_length])
set_M_length = int(input())
set_M = set(list(map(int, input().split()))[0:set_M_length])

left_symmetric_difference = set_N.difference(set_M)
right_symmetric_difference = set_M.difference(set_N)

all_numbers = list(left_symmetric_difference.union(right_symmetric_difference))

for number in sorted(all_numbers):
    print(number)
