import numpy as np

F1=350.0
F2=300.0
F3=700.0
M=1100.0
theta=40.0
 
fx = F1 * np.cos(np.radians(60)) - F3 * np.sin(np.radians(theta))
fy = -(F1 * np.sin(np.radians(60)) + F2 + F3 * np.cos(np.radians(theta)))

print('fx =', fx, 'N')
print('fy =', fy, 'N')
#fr=(fx**2+fy**2)**0.5
mr=2*F1*np.sin(np.radians(60))+F2*6+9*F3*np.cos(np.radians(theta))+M
x=mr/np.abs(fy)
print('x =', x, 'm')