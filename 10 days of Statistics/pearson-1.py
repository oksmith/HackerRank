N = int(input())
X = list(map(float,input().split()))
Y = list(map(float,input().split()))

def pearsonCorrCoef(X,Y):
    mu_X = sum(X)/len(X)
    mu_Y = sum(Y)/len(Y)
    sigma_X = (sum([(x-mu_X)**2 for x in X])/len(X))**0.5
    sigma_Y = (sum([(y-mu_Y)**2 for y in Y])/len(Y))**0.5
    xy = [(x - mu_X)*(y - mu_Y) for x,y in zip(X,Y)]
    sumxy = sum(xy)
    rho = sumxy/(len(X)*sigma_X*sigma_Y)
    return(rho)

print("{:.03f}".format(pearsonCorrCoef(X,Y)))
