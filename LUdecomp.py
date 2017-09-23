#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 11:46:48 2017

@author: terri
"""
import scipy
import scipy.sparse 
import scipy.sparse.linalg 
import matplotlib 
import numpy as np
import scipy.linalg


##SET UP MARTIX A
i = 100
A = np.zeros(shape=(i,i))
        
Range1=np.arange(i)
Range2=np.arange(i-1)
Range3=np.arange(i-int(i/2))

A[Range1,Range1] = -4
A[Range2+1,Range2] =1
A[Range2,Range2+1]=1
A[Range3,Range3+int(i/2)]=1
A[Range3+int(i/2), Range3]=1
## END SETUP

## SET UP b and c
i = 100
b= np.zeros(shape=(i, 1))
c= np.zeros(shape=(i, 1))

for k in range (0,100):
    b[k][0]=1

for k in range (0,100):
    c[k][0]=k
## END SETUP

A = scipy.sparse.csc_matrix(A)

lu  = scipy.sparse.linalg.splu(A)

result_b = lu.solve(b)
result_c = lu.solve(c)

#print(result_b)
#print(result_c)

L = lu.L.A
U = lu.U.A
#print (U)

matplotlib.pyplot.spy(A)
