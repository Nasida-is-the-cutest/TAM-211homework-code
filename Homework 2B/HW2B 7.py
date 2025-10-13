import numpy as np
a=60
b=120
c=45
f=814
lx=0.4
ly=0.5
lz=-0.3
l=np.array([lx,ly,lz])
f=np.array([f*np.cos(np.radians(a)),f*np.cos(np.radians(b)),f*np.cos(np.radians(c))])
m=np.cross(l,f)
print("m=",m)