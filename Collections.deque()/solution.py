from collections import deque

d = deque()
num_of_operations = int(input())
for _ in range(num_of_operations):
    method_with_value = input().split()
    try:
        method_to_deque, value_to_deque = method_with_value[0], int(method_with_value[1])
    except IndexError:
        method_to_deque = method_with_value[0]

    if method_to_deque == 'append':
        d.append(value_to_deque)
    elif method_to_deque == 'pop':
        d.pop()
    elif method_to_deque == 'popleft':
        d.popleft()
    elif method_to_deque == 'appendleft':
        d.appendleft(value_to_deque)
    else:
        continue
for item in list(d):
    print(item, end=" ")

