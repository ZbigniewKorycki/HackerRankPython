def operations_of_set():
    len_starting_set = int(input())
    starting_set = set(list(map(int, input().split()))[0:len_starting_set])

    for _ in range(int(input())):
        command, num_of_elements_in_set = input().split()
        another_set = set(list(map(int, input().split()))[0:int(num_of_elements_in_set)])
        if command == 'intersection_update':
            starting_set.intersection_update(another_set)
        elif command == 'update':
            starting_set.update(another_set)
        elif command == 'symmetric_difference_update':
            starting_set.symmetric_difference_update(another_set)
        elif command == 'difference_update':
            starting_set.difference_update(another_set)
        else:
            continue
    print(sum(list(starting_set)))


if __name__ == "__main__":
    operations_of_set()


