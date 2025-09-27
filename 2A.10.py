# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 15:40:03 2025

@author: 1
"""

import numpy as np

s1  = 0.5 # m
s2  = 0.4 # m
a  = 5.0 # m
b  = 2.0 # m
k1  = 300.0 # N/m
f1=((a**2+(b+s1)**2)**0.5-(a**2+b**2)**0.5)*k1
cosa=a/(a**2+(b+s1)**2)**0.5
sina=(b+s1)/(a**2+(b+s1)**2)**0.5
cosc=a/(a**2+(b+s2)**2)**0.5
sinc=(b+s2)/(a**2+(b+s2)**2)**0.5
cosb=1/(1+(s2-s1)**2)**0.5
sinb=(s1-s2)/(1+(s2-s1)**2)**0.5
f2=f1*cosa/cosc
f=f1*cosa/cosb
A=(f1*sina+f*sinb)/9.8
print("A=",A)
B=(f2*sinc-f*sinb)/9.8
print("B=",B)
