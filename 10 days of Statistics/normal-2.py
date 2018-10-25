mu = 70
sigma = 10

# P(X>80) = P(Z>(80-70)/10) = 1-norm.cdf((80-70)/10)
# P(X>60) = 1-norm.cdf((80-60)/10)
# P(X<60) = norm.cdf((80-60)/10)

from scipy.stats import norm

p1 = 1-norm.cdf((80-70)/10)
p2 = 1-norm.cdf((60-70)/10)
p3 = norm.cdf((60-70)/10)


print("{:.04f}".format(p1))
print("{:.04f}".format(p2))
print("{:.04f}".format(p3))
