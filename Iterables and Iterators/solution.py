from itertools import combinations

length = int(input())
element_of_list = input().split()
number_of_indices = int(input())

result = list(combinations(element_of_list, r=number_of_indices))

counter = 0
for item in result:
    if "a" in item:
        counter += 1

print(round(counter/len(result), 3))



