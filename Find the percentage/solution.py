from statistics import mean
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores_of_query_student = student_marks.get(query_name)
    average_scores = float(mean(scores_of_query_student))
    print("%.2f" % average_scores)