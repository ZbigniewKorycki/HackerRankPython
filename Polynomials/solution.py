import numpy

values_P = list(map(float, input().split()))
x = int(input())

print(numpy.polyval(values_P, x))