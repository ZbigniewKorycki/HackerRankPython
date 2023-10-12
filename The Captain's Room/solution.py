from collections import Counter

size_of_each_group = int(input())
hotels_room_for_each_tourist = list(map(int, input().split()))
hotels_room_usage_counter = Counter(hotels_room_for_each_tourist)

for room, usage in dict(hotels_room_usage_counter).items():
    if usage == 1:
        print(room)
        break

