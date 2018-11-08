#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    N = len(arr)
    zeroes = sum( 1 for a in arr if a == 0)
    pos = sum( 1 for a in arr if a > 0 )
    neg = sum( 1 for a in arr if a < 0 )
    print(pos/N)
    print(neg/N)
    print(zeroes/N)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
