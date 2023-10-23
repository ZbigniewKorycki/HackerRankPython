from collections import Counter

num_of_elements_in_array_n, num_of_elements_in_sets = list(map(int, (input().split())))

array_n = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

counted_array = dict(Counter(array_n))

happiness = 0

for number, occurrence in counted_array.items():
    if number in set_a:
        happiness += occurrence
    elif number in set_b:
        happiness -= occurrence
    else:
        continue

print(happiness)

