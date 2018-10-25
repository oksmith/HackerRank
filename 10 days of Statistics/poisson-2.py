import math

lambA = 0.88
lambB = 1.55

def C_A(x):
    return(160 + 40*x)
def C_B(y):
    return(128 + 40*y)

#variance is lambda => E(X^2) = lambda + lambda^2
EX_2 = lambA + lambA**2
EY_2 = lambB + lambB**2

print("{:.03f}".format(C_A(EX_2)))
print("{:.03f}".format(C_B(EY_2)))
