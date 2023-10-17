if __name__ == "__main__":
    num_students, num_subjects = list(map(int, input().split()))
    all_students_marks = []

    marks = [list(map(float, input().split())) for _ in range(num_subjects)]

    average = [print(sum(student_marks)/num_subjects) for student_marks in list(zip(*marks))]


