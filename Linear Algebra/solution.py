import numpy

N = int(input())

values_of_matrix = [list(map(float, input().split()))[0:N] for _ in range(N)]

print(round(numpy.linalg.det(values_of_matrix), 2))

