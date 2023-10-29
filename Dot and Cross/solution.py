import numpy

size_of_N = int(input())

values_a = list()
values_b = list()

for row in range(size_of_N):
    row_values = list(map(int, input().split()))[0:size_of_N]
    values_a.append(row_values)

for row in range(size_of_N):
    row_values = list(map(int, input().split()))[0:size_of_N]
    values_b.append(row_values)

array_a = numpy.array(values_a)
array_b = numpy.array(values_b)

print(numpy.dot(array_a, array_b))

