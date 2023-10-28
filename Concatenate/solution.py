import numpy

size_n, size_m, size_p = list(map(int, input().split()))

values_of_n = list()

for _ in range(size_n):
    row = list(map(int, input().split()))
    values_of_n.append(row)

values_of_m = list()
for _ in range(size_m):
    row = list(map(int, input().split()))
    values_of_m.append(row)


print(numpy.concatenate((values_of_n, values_of_m), axis=0))
