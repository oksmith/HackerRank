N = int(input())
X = [int(s) for s in input().split(" ")]
X = sorted(X)

mean = sum(X)/len(X)
if len(X)%2 == 1:
    median = X[(len(X)-1)/2]
        # remember that python lists start indexing at 0, not 1 (like in R)
else:
    median = (X[int(len(X)/2-1)]+X[int(len(X)/2)])/2
mode = max(X,key=X.count)

print("{:0.1f}".format(mean))
print("{:0.1f}".format(median))
print(mode)
