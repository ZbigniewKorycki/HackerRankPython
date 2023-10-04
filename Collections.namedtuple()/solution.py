from collections import namedtuple

marks_sum = 0

student_list = int(input())
column_names = list(map(str,input().split()))
Student = namedtuple("Student", column_names)
for number_of_students in range(student_list):
    mark_info = list(map(str, input().split()))
    student = Student(mark_info[0], mark_info[1], mark_info[2], mark_info[3])
    marks_sum += int(student.MARKS)

print(marks_sum/student_list)
