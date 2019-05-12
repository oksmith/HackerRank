import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    results = []
    
    seqList = [[] for i in range(n)]
    lastAnswer = 0
    
    for query in queries:
        x = query[1]
        y = query[2]
        index = (x ^ lastAnswer) % n
        #print(index)
        if query[0] == 1:
            seqList[index].append(y)
        elif query[0] == 2: 
            seq = seqList[index]
            size = len(seq)
            lastAnswer = seq[y%size]
            results.append(lastAnswer)
        else: 
            print("Query not 1 or 2")
    
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for i in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
