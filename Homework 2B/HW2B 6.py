import numpy as np
x=-0.25
y=0.25*(3)**0.5-0.5
z=0.5
f=452
l=(x**2+y**2+z**2)**0.5
fx=f*x/l
fy=f*y/l
fz=f*z/l
f_hat=np.array([fx,fy,fz])
x=np.array([0,0.5*3**0.5,0.5])
m=np.cross(x,f_hat)
print("m=",m)

