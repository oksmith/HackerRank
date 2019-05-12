p = 0.12
    # this is the probability of rejection

N = 10
    # number of children in a family

# Assume X ~ Binom(N,p). 
import math

def b(x,N,p):
    ncr=(math.factorial(N)/(math.factorial(x)*math.factorial(N-x)))
    temp = (p**x)*((1-p)**(N-x))
    return(ncr*temp)
    
# P(X<3)  
q=0
for x in range(0,3):
    q += b(x,N,p)

# P(X>1)
r=0
for x in range(2,N+1):
    r += b(x,N,p)

print("{0:.3f}".format(q))
print("{0:.3f}".format(r))
