num_of_students_english = int(input())
students_roll_english = set(map(int, input().split()))
num_of_students_french = int(input())
students_roll_french = set(map(int, input().split()))

students_with_at_least_one_subscription = students_roll_english.union(students_roll_french)

print(len(students_with_at_least_one_subscription))
