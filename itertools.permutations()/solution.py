from itertools import permutations


def print_permutation(string_with_length):
    permutation_string = list(string_with_length[0])
    permutation_length = int(string_with_length[1])
    permutation_string.sort()
    for item in list(permutations(permutation_string, permutation_length)):
        print(''.join(list(item)))


if __name__ == '__main__':
    user_input = input().split()
    print_permutation(user_input)

