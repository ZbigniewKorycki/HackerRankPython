if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

runner_up_score = list(arr)

list_number = []
for number in runner_up_score:
    list_number.append(number)

runner_up_score_sorted = list(set(list_number))
runner_up_score_sorted.sort()
runner_up_score_sorted = runner_up_score_sorted[-2]
print(runner_up_score_sorted)
