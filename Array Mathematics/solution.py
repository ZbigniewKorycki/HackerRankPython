import numpy

N, M = list(map(int, input().split()))

array_A = numpy.array([list(map(int, input().split()))[0:M] for _ in range(N)])
array_B = numpy.array([list(map(int, input().split()))[0:M] for _ in range(N)])

print(numpy.add(array_A, array_B))
print(numpy.subtract(array_A, array_B))
print(numpy.multiply(array_A, array_B))
print(numpy.floor_divide(array_A, array_B))
print(numpy.mod(array_A, array_B))
print(numpy.power(array_A, array_B))