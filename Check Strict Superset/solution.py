set_A = set(list(map(int, input().split())))
num_of_other_sets = int(input())

def check_strict_superset(core_set, number_of_other_sets):
    for _ in range(number_of_other_sets):
        set_to_compare = set(list(map(int, input().split())))
        if core_set.issuperset(set_to_compare) and core_set != set_to_compare:
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    print(check_strict_superset(set_A, num_of_other_sets))
