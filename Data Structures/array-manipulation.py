#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0 for i in range(n)]
    array_list = [array]
    
    for query in queries:
        st = int(query[0])
        end = int(query[1])
        for i in range(st-1,end):
            array[i] = array[i] + query[2]
        array_list.append(array)
    
    return(max([num for array in array_list for num in array]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
