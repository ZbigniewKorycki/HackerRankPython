import collections


def check_pilling_up(length_of_cubes_side):
    pile = list()
    queue = collections.deque(length_of_cubes_side)
    for _ in range(len(queue)):
        if queue[0] >= queue[-1]:
            if len(pile) == 0 or queue[0] <= pile[-1]:
                pile.append(queue[0])
                queue.popleft()
            else:
                return False
        else:
            if len(pile) == 0 or queue[-1] <= pile[-1]:
                pile.append(queue[-1])
                queue.pop()
            else:
                return False
    return True


if __name__ == "__main__":
    number_of_test_cases = int(input())
    for x in range(number_of_test_cases):
        number_of_cubes = int(input())
        cubes_side_length = list(map(int, input().split()))[0:number_of_cubes]
        result = check_pilling_up(cubes_side_length)
        if result:
            print("Yes")
        else:
            print("No")