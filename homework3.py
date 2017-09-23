#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 12:32:19 2017

@author: terri
"""
import scipy
import matplotlib as plot
import numpy as np
from scipy import linalg
cond = np.empty(49, dtype=object)
x = np.empty(49, dtype=object)
for j in range (2, 51):
    x[j-2]=j


for i in range(2,51):
    A = np.zeros(shape=(i,i))
    Range1=np.arange(i)
    Range2=np.arange(i-1)
    Range3=np.arange(i-int(i/2))
    
    A[Range1,Range1] = -2
    A[Range2+1,Range2] =1
    A[Range2,Range2+1]=1
    cond[i-2] = np.linalg.cond(A, p=None)
plot.pyplot.plot(x, cond, 'bo')