N = int(input())
X = list(map(int,input().split(" ")))
F = list(map(int,input().split(" ")))

S = []
for i in range(N):
    for f in range(F[i]):
        S.append(X[i])
S.sort()

def find_median(lst,start,end):
    median = 0
    length = end - start + 1
    if (length % 2 == 0):
        median = float(lst[int(start + length / 2 - 1)] + lst[int(start + length / 2)]) / 2
    else:
        median = float(lst[int(start + (length - 1) / 2)])
    return(median)

n = len(S)
if n % 2 == 0:
    q1 = find_median(S,0,n/2-1)
    q3 = find_median(S,n/2,n-1)
else:
    q1 = find_median(S,0,(n-1)/2-1)
    q3 = find_median(S,(n-1)/2,n)

print(q3 - q1)

    
