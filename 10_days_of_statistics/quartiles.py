N = int(input())
lst = list(map(int, input().split(" ")))
lst.sort()

def find_median(lst,start,end):
    median = 0
    length = end - start + 1
    if (length % 2 == 0):
        median = (lst[int(start + length / 2 - 1)] + lst[int(start + length / 2)]) / 2
    else:
        median = lst[int(start + (length - 1) / 2)]
    return(median)
    
q2 = find_median(lst,0,N-1)
if N % 2 == 0:
    q1 = find_median(lst,0,N/2-1)
    q3 = find_median(lst,N/2,N-1)
else:
    q1 = find_median(lst,0,(N-1)/2 - 1)
    q3 = find_median(lst,(N-1)/2,N)
    
print(int(q1))
print(int(q2))
print(int(q3))
