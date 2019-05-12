mu = 20
sigma = 2

# p1 = P(X<19.5) = P(Z < (19.5 - 20)/2)

from scipy.stats import norm

p1 = norm.cdf((19.5-20)/2)
qa = norm.cdf(0)
qb = norm.cdf((22 - 20)/2)

print("{:.03f}".format(p1))
print("{:.03f}".format(qb-qa))
