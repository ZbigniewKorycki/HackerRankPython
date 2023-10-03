from collections import Counter

num_of_shoes = int(input())
shoes_size = list(map(int, input().split()))
num_of_clients = int(input())
shoes_size_with_count = Counter(shoes_size)
money_earned = 0
for _ in range(num_of_clients):
    client_request = list(map(int, input().split()))
    if client_request[0] in shoes_size_with_count.elements():
        requested_shoes = Counter({client_request[0]: 1})
        shoes_size_with_count.subtract(requested_shoes)
        money_earned += client_request[1]
        continue
    else:
        continue

print(money_earned)