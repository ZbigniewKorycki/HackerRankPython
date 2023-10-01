from itertools import product

A_raw = input("Numbers for list A: ").split()
B_raw = input("Numbers for list B: ").split()

list_A = [int(n) for n in A_raw]
list_B = [int(n) for n in B_raw]

combined_list_AB = list(product(list_A, list_B))

cartesian_product = ' '.join([str(item) for item in combined_list_AB])
print(cartesian_product)
