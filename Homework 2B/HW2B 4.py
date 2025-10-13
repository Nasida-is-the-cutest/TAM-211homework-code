import numpy as np
import sympy as sp
a  = 1.000 # 
b  = 3.000 # 
c  = 0.800 # 
l  = 9.000 # ft
x = sp.Symbol('x')
f1 = a+b*x**c
I1 = sp.integrate(f1, (x, 0, l))
print("F =", I1)
f2 = f1 * x
I2 = sp.integrate(f2, (x, 0, l))
x_hat = I2 / I1
print("x =", x_hat)