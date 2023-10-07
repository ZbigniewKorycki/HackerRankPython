students_english_subscription = int(input())
students_english_subscription_roll_numbers = list(map(int, input().split()))[0:students_english_subscription]

students_french_subscription = int(input())
students_french_subscription_roll_numbers = list(map(int, input().split()))[0:students_french_subscription]

students_roll_numbers_only_one_subscription = set(students_french_subscription_roll_numbers).symmetric_difference(set(students_english_subscription_roll_numbers))

print(len(students_roll_numbers_only_one_subscription))
