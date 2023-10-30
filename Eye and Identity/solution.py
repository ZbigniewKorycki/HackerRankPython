import numpy

numpy.set_printoptions(legacy='1.13')

nr_rows, nr_columns = list(map(int, input().split()))

print(numpy.eye(nr_rows, nr_columns))