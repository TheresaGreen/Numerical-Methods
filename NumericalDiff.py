#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:59:44 2017

@author: terri
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def fPrime(x):
    return np.cos(x)

def fAprox(x, e):
    return (f(x + e)-f(x))/e

def h(y):
    return np.exp(-y)

n = np.linspace(0,40, num=70)

#plt.plot(h(n), np.abs(fAprox(2.0, h(n))-fPrime(2.0)))

plt.loglog(h(n), np.abs(fAprox(2.0, h(n))-fPrime(2.0)), 'bo')
plt.show()
 
print('Observations: The smallest h(n) starts out with a bad error but as it  ')
print('gets bigger the error starts to get smaller. then at a certain point it ')
print('turns and the error becomes bigger again.')
print('Explanation: the smallest h has a bad error due to a cancellation error ')
print('(because two numbers very close to each other will give a horrible error) ')
print('but as h gets larger the error will improve. However at a certain point h will ')
print('be too big so it will no longer be a good approximation, and that is when the error begins to grow again.')
print('The bottom most point of the triangle shape would be the best size of h to use.')
print('The h is big enough to avoid cancelation errors, but is still a good approximation')