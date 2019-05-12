N = int(input())
X = list(map(float,input().split()))
Y = list(map(float,input().split()))

# thank you to ubutnu's code for getting the rank
def rank_simple(vector):
    return sorted(range(len(vector)), key=vector.__getitem__)

def rankdata(a):
    n = len(a)
    ivec=rank_simple(a)
    svec=[a[rank] for rank in ivec]
    sumranks = 0
    dupcount = 0
    newarray = [0]*n
    for i in range(n):
        sumranks += i
        dupcount += 1
        if i==n-1 or svec[i] != svec[i+1]:
            averank = sumranks / float(dupcount) + 1
            for j in range(i-dupcount+1,i+1):
                newarray[ivec[j]] = averank
            sumranks = 0
            dupcount = 0
    return newarray

def pearsonCorrCoef(X,Y):
    mu_X = sum(X)/len(X)
    mu_Y = sum(Y)/len(Y)
    sigma_X = (sum([(x-mu_X)**2 for x in X])/len(X))**0.5
    sigma_Y = (sum([(y-mu_Y)**2 for y in Y])/len(Y))**0.5
    xy = [(x - mu_X)*(y - mu_Y) for x,y in zip(X,Y)]
    sumxy = sum(xy)
    rho = sumxy/(len(X)*sigma_X*sigma_Y)
    return(rho)

rankX = rankdata(X)
rankY = rankdata(Y)
print("{:.03f}".format(pearsonCorrCoef(rankX,rankY)))
