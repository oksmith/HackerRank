#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    ar.sort()
    largest = ar[len(ar)-1]
    count = 1
    stop = False
    while stop == False:
        if ar[len(ar)-1-count] == largest:
            count += 1
            if count == len(ar):
                stop = True
        else: 
            stop = True
    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
