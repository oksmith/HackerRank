import math
from scipy.stats import norm

max_ = 9800
mu = 205
sigma= 15
N = 49

# Pr(sum(X_i) < max) = Pr(sum(X_i)/N < max/N) 
#    = Pr(sqrt(N)*(sum(X_i)/N - mu) < sqrt(N)*(max/N - mu))
t = math.sqrt(N)*(max_/N - mu)

# note sqrt(N)*(sum(X_i)/N - mu) is approximately N(0,sigma^2)
# p = Pr(Z<t/sigma)
print("{:.04f}".format(norm.cdf(t/sigma)))
