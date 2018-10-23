#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0 for i in range(n)]
    MAX = 0
    
    for query in queries:
        for i in range(int(query[0])-1,int(query[1])):
            array[i] = array[i] + query[2]
        max_ = max(array)
        if max_>MAX:
            MAX = max_ 
    
    return(MAX)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for i in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
