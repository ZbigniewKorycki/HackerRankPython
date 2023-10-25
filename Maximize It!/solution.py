from itertools import product

K, M = list(map(int, input().split()))

all_elements = []

for _ in range(K):
    list_x = list(map(int, input().split()))[1:]
    all_elements.append(list_x)

cartesian_product = list(product(*all_elements))

S_max = 0
for elements in cartesian_product:
    sum_of_powers = sum([pow(x, 2) for x in elements])
    rest_after_modulo = sum_of_powers % M
    if rest_after_modulo > S_max:
        S_max = rest_after_modulo

print(S_max)
