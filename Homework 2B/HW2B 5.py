import numpy as np
import scipy as sp
theta  = 24.0 # deg
P  = 170.0 # lb
a  = 5.0 # in
b  = 5.0 # in
t1=np.radians(90-45-theta)
t2=np.radians(45+theta)
p1=np.radians(45-theta)
p2=np.radians(45+theta)
def func(f):
    fd=f*(b*np.sin(t1)+a*np.sin(t2))
    pd=P*2*(b*np.sin(p1)-a*np.sin(p2))
    fun=fd+pd
    return fun
F=sp.optimize.fsolve(func,1)
print("F=",F)