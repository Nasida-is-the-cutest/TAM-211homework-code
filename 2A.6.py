# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 16:46:31 2025

@author: 1
"""

from scipy.optimize import brentq
import numpy as np

p  = 10.0 # lb
a  = 2# ft
k  = 10.0 # lb/ft
#设要求的角度是x

def f(x):
    f2=k*(((2*a-a*np.cos(x))**2+(a*np.sin(x))**2)**0.5-a)
    y=np.arctan(a*np.sin(x)/(2*a-a*np.cos(x)))
    f=f2*np.cos(y)*np.sin(x)/np.cos(x)+f2*np.sin(y)-p
    return f
root = brentq(f, 0, 7)
angle=root/np.pi*180
print(angle)



