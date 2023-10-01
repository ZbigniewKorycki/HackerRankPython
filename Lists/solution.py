def insert_int(command, my_list):
    e = int(command.split()[2])
    i = int(command.split()[1])
    my_list.insert(i, e)
    return my_list


def print_num(my_list):
    print(my_list)


def remove_int(command, my_list):
    e = int(command.split()[1])
    my_list.remove(e)
    return my_list


def append_int(command, my_list):
    e = int(command.split()[1])
    my_list.append(e)
    return my_list


def sort_list(my_list):
    my_list.sort()
    return my_list


def pop_num(my_list):
    my_list.pop()
    return my_list


def reverse_list(my_list):
    my_list.reverse()
    return my_list


if __name__ == '__main__':
    N = int(input())
    num_list = []
    for command_num in range(N):
        command = input()
        command_word = command.split()[0]
        if command_word == "insert":
            num_list = insert_int(command, num_list)
        elif command_word == "print":
            print_num(num_list)
        elif command_word == "remove":
            num_list = remove_int(command, num_list)
        elif command_word == "append":
            num_list = append_int(command, num_list)
        elif command_word == "sort":
            num_list = sort_list(num_list)
        elif command_word == "pop":
            num_list = pop_num(num_list)
        elif command_word == "reverse":
            num_list = reverse_list(num_list)