a=0.05
L=0.106
b=0.1
len=(L**2+(b+a)**2)**0.5
f=30
m=f*len
print("Mmax=",m)
import numpy as np
#l_hat=np.array([-L,0,a+b])
Alpha=np.arctan(L/(a+b))/np.pi*180
Gamma=np.arctan((a+b)/L)/np.pi*180
print("Alpha=",Alpha)
print("Beta=","90")
print("Gamma=",Gamma)
