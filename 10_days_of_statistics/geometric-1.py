p = 1/3
    # this is the probability of rejection

#N = 10


def c(x,p):
    temp = p*((1-p)**(x-1))
    return(temp)
    
# P(first rejection on x=5)  

print("{0:.3f}".format(c(5,p)))
