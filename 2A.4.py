# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 14:22:44 2025

@author: 1
"""

import numpy as np
f1sin=7*np.cos(70/180*np.pi)+5*np.sin(30/180*np.pi)-21/5
f1cos=5*np.cos(30/180*np.pi)-7*np.sin(70/180*np.pi)+28/5
tan=f1sin/f1cos
bata=np.arctan(tan)
print(bata*180/np.pi)
f=f1sin/np.sin(bata)
print(f)