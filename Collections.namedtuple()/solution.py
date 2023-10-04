from collections import namedtuple

students_num = int(input())
fields = input().split()
Student = namedtuple("Student", fields)
print(round(sum([int(input().split()[fields.index("MARKS")]) for _ in range(students_num)]) / students_num, 2))

