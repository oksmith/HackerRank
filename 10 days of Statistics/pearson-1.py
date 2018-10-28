N = int(input())
X = list(map(float,input().split()))
Y = list(map(float,input().split()))

mu_X = 6.73
sigma_X = 2.39251
mu_Y = 37.8
sigma_Y = 55.1993

def pearsonCorrCoef(X,Y,mu_X,mu_Y):
    xy = [(x - mu_X)*(y - mu_Y) for x,y in zip(X,Y)]
    sumxy = sum(xy)
    rho = sumxy/(N*sigma_X*sigma_Y)
    return(rho)

print("{:.03f}".format(pearsonCorrCoef(X,Y,mu_X,mu_Y)))
