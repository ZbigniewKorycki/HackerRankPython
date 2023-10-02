num_of_students_english = int(input())
students_roll_english = set(map(int, input().split()))
num_of_students_french = int(input())
students_roll_french = set(map(int, input().split()))

students_with_only_english_subscription = students_roll_english.difference(students_roll_french)

print(len(students_with_only_english_subscription))
