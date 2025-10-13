import numpy as np
import scipy as sp
r  = 3.0 # m
M  = 1300.0 # Nm
a  = 5.0 # m
theta  = 45.0 # deg
t=theta*np.pi/180
ab=np.array([r*np.sin(t),0, r*np.cos(t)-r])
bc=np.array([a-r*np.sin(t),a, -np.cos(t)*r])

norm_bc = np.linalg.norm(bc)
norm_ab = np.linalg.norm(ab)

def f(F):
    f=F*bc/norm_bc
    m=np.cross(ab,f)
    e=np.linalg.norm(m)-M
    return e
F = sp.optimize.fsolve(f, 1)
print("F =", F)