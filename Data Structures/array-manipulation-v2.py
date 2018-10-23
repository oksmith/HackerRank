#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import accumulate

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0 for i in range(n)]
    
    for query in queries:
        first_index = int(query[0])-1
        last_index = int(query[1])-1
        array[first_index] += query[2]
        if last_index+1 < n:
            array[last_index+1] += -query[2]
    
    cumsum = accumulate(array) 
    MAX = max(cumsum)
    
    return(MAX)

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
