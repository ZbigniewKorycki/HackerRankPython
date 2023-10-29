import numpy

N, M = list(map(int, input().split()))

values_of_NxM = []
for _ in range(N):
    row = list(map(int, input().split()))
    values_of_NxM.append(row)

array_NxM = numpy.array(values_of_NxM)
sum_of_array = numpy.sum(array_NxM, axis=0)
print(numpy.prod(sum_of_array))



