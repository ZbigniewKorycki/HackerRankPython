def mutate_string(string, position, character):
    mutate_list = list(string)
    mutate_list[position] = character
    output_string = "".join(mutate_list)
    return output_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)