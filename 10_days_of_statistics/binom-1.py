
n=1.09
m=1
p = n/(n+m)
    # this is the probability of giving birth to a boy

N = 6
    # number of children in a family

# Assume X ~ Binom(N,p). We want q = P(X>3)
import math

def b(x,N,p):
    ncr=(math.factorial(N)/(math.factorial(x)*math.factorial(N-x)))
    temp = (p**x)*((1-p)**(N-x))
    return(ncr*temp)
    
q=0
for x in range(3,N+1):
    q += b(x,N,p)

print("{0:.3f}".format(q))
