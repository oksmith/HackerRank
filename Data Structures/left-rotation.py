#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    
    at = a[0:d]
    for i in range(d):
        a.pop(0)
    
    a = a + at
    print(" ".join([str(l) for l in a]))
