def get_number_of_items_in_set():
    length_of_set = int(input())
    return length_of_set


def get_starting_set(length_of_set):
    starting_set = set(list(map(int, input().split()))[0:length_of_set])
    return starting_set


def get_number_of_commands():
    number_of_commands = int(input())
    return number_of_commands


def process_commands(number_of_commands, starting_set):
    set_processed = starting_set
    for _ in range(number_of_commands):
        command_with_number = input()
        command = command_with_number.split()[0]
        if command == "remove":
            remove_item(set_processed, command_with_number)
        elif command == "discard":
            discard_item(set_processed, command_with_number)
        elif command == "pop":
            pop_item(set_processed)
    return set_processed


def remove_item(given_set, input_command):
    command, number = input_command.split()
    given_set.remove(int(number))
    return given_set


def discard_item(given_set, input_command):
    command, number = input_command.split()
    given_set.discard(int(number))
    return given_set


def pop_item(given_set):
    given_set.pop()
    return given_set


def start_process():
    num_of_items = get_number_of_items_in_set()
    starting_set = get_starting_set(num_of_items)
    num_of_commands = get_number_of_commands()
    final_set = process_commands(num_of_commands, starting_set)
    print(sum(final_set))


start_process()
