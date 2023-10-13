num_of_items_in_numbers = int(input())
numbers = list(map(int, input().split()))[0:num_of_items_in_numbers]
print((all(num > 0 for num in numbers) and (any(str(num) == str(num)[::-1] for num in numbers))))





