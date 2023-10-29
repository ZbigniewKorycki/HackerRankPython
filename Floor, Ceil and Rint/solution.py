import numpy
numpy.set_printoptions(legacy='1.13')

array_x = numpy.array(list(map(float, input().split())))

print(numpy.floor(array_x))
print(numpy.ceil(array_x))
print(numpy.rint(array_x))

