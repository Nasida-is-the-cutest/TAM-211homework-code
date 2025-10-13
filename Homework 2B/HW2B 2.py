# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 16:10:11 2025

@author: 1
"""
import numpy as np
import sympy as sp

w1 = 9.0  # kips/ft
w2 = 3.0  # kips/ft
a = 24.0  # ft
b = 11.0  # ft

lab = (a**2 + b**2)**0.5
fr = (w1 + w2)/2 * lab
print("fr =", fr)

x = sp.Symbol('x')
f1 = (w2 - w1)/lab * x + w1
print("计算I1...")
I1 = sp.integrate(f1, (x, 0, lab))
print("I1计算完成")
f2 = f1 * x
print("计算I2...")
I2 = sp.integrate(f2, (x, 0, lab))
print("I2计算完成")

x_hat = I2 / I1
print("x_hat =", x_hat)