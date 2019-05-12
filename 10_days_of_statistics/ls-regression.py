math_mark = [95,85,80,70,60]
stats_mark = [85,95,70,65,70]

mu_X = sum(math_mark)/len(math_mark)
mu_Y = sum(stats_mark)/len(stats_mark)
sigma_X = (sum([(x-mu_X)**2 for x in math_mark])/len(math_mark))**0.5
sigma_Y = (sum([(y-mu_Y)**2 for y in stats_mark])/len(stats_mark))**0.5
    
def pearsonCorrCoef(X,Y):
    mu_X = sum(X)/len(X)
    mu_Y = sum(Y)/len(Y)
    sigma_X = (sum([(x-mu_X)**2 for x in X])/len(X))**0.5
    sigma_Y = (sum([(y-mu_Y)**2 for y in Y])/len(Y))**0.5
    xy = [(x - mu_X)*(y - mu_Y) for x,y in zip(X,Y)]
    sumxy = sum(xy)
    rho = sumxy/(len(X)*sigma_X*sigma_Y)
    return(rho)

b = pearsonCorrCoef(math_mark,stats_mark)*sigma_Y/sigma_X
a = mu_Y - b*mu_X

print("{:.03f}".format(a + b*80))
