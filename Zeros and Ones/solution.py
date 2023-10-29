import numpy

sizes = list(map(int, input().split()))

print(numpy.zeros(shape=sizes, dtype=int))
print(numpy.ones(shape=sizes, dtype=int))
