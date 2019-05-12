import math
from scipy.stats import norm

mu = 500
sigma= 80
N = 100

# Pr(A < sum(X_i)/n < B) = Pr( sqrt(N)*(A-mu)/sigma < Z < sqrt(N)*(B-mu)/sigma) = 0.95
# => sqrt(N)*(B-mu)/sigma = 1.96 and sqrt(N)*(A-mu)/sigma = -1.96

A = mu - 1.96*sigma/math.sqrt(N)
B = mu + 1.96*sigma/math.sqrt(N)


print("{:.02f}".format(A))
print("{:.02f}".format(B))
