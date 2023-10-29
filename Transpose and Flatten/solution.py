import numpy

N, M = list(map(int, input().split()))

array_x = numpy.array([list(map(int, input().split()))[0:M] for _ in range(N)])

print(array_x.transpose())
print(array_x.flatten())