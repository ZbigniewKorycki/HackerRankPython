num_students_English_newsletter = int(input())
roll_numbers_students_English_newsletter = set(input().split()[0:num_students_English_newsletter])

num_students_French_newsletter = int(input())
roll_numbers_students_French_newsletter = set(input().split()[0:num_students_French_newsletter])

print(len(roll_numbers_students_French_newsletter.intersection(roll_numbers_students_English_newsletter)))
