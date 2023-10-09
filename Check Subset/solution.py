num_of_test_cases = int(input())

for _ in range(num_of_test_cases):
    num_elements_in_A = int(input())
    element_of_A = set(list(input().split())[0:num_elements_in_A])
    num_elements_in_B = int(input())
    element_of_B = set(list(input().split())[0:num_elements_in_B])
    print(element_of_A.issubset(element_of_B))


