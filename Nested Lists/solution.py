if __name__ == '__main__':
    python_students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])

    only_score = list(set([i[1] for i in python_students]))
    only_score.sort()
    second_lowest_score = only_score[1]

    names_of_students_with_second_lowest_score = []
    for i in python_students:
        if i[1] == second_lowest_score:
            names_of_students_with_second_lowest_score.append(i[0])

    names_of_students_with_second_lowest_score.sort()

    for name in names_of_students_with_second_lowest_score:
        print(name)