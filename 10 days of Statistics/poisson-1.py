import math

lamb = 2.5
k = 5

def p(lamb, k):
    fc = math.factorial(k)
    pr = (lamb**k)*math.exp(-lamb)
    return(pr/fc)

print(p(lamb,k))
