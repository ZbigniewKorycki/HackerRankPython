import numpy

list_of_integers = list(map(int, input().split()))

my_array = numpy.array(list_of_integers)

print(numpy.reshape(my_array, (3,3)))