
#legendre polynomial
#(4) n*P(n-1,x) = P'(n,x)-x*P'(n-1,x)

import numpy as np
from scipy.special import legendre
from scipy.misc import derivative

x=float(input("Enter the x: "))
n=int(input("Enter the n: "))

def f(x):
    return legendre(n)(x)
def g(x):
    return legendre(n-1)(x)
LHS=derivative(f,x,order=15)
RHS=x*derivative(g,x,order=15)+n*g(x)
print("LHS: ",LHS)
print("RHS: ",RHS)

