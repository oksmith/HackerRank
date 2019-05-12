#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    chars_1 = list(s1)
    chars_2 = list(s2)
    lngth = len(set(chars_1)) + len(set(chars_2))
    st = set(chars_1 + chars_2)
    if (len(st) == lngth):
        return("NO")
    else: 
        return("YES")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
