import numpy

N, M = list(map(int, input().split()))

values = [list(map(int, input().split()))[0:M] for _ in range(N)]

array_x = numpy.array(values)

min_array_x = numpy.min(array_x, axis=1)

print(numpy.max(min_array_x, axis=0))