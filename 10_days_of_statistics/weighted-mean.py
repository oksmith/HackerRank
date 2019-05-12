N = int(input())
X = [int(s) for s in input().split(" ")]
W = [int(s) for s in input().split(" ")]

tot_weight = sum(W)
mult = [x*w for x,w in zip(X,W)]
    # zip function: returns a list of tuples (x,w) 
wtd_avg = sum(mult)/sum(W)

print("{:0.1f}".format(wtd_avg))
