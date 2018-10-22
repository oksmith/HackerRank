#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag_dict = {}
    note_dict = {}
    
    for word in magazine:
        if word not in mag_dict:
            mag_dict[word] = 0
        mag_dict[word] += 1
        
    for word in note:
        if word not in note_dict:
            note_dict[word] = 0
        note_dict[word] += 1
    
    result = True
    for word in note_dict.keys():
        if word not in mag_dict.keys():
            result = False
        elif note_dict[word] > mag_dict[word]:
            result = False
    
    yn = "Yes" if result == True else "No"
    print(yn)
            

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
