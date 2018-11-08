#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    ampm = s[len(s)-2:len(s)]
    hour = int(s[0:2])%12
    if ampm == "AM":
        if hour<10:
            hr = "0" + str(hour)
        else:
            hr = str(hour)
        return(hr + str(s[2:len(s)-2]))
    else:
        hr = str(hour+12)
        return(hr + str(s[2:len(s)-2]))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
