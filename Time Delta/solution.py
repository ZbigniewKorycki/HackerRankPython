import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    date1 = datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    date2 = datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    difference = date1-date2
    return str(abs(int(difference.total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

# Sun 10 May 2015 13:54:36 -0700
