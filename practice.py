#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 14:41:51 2017

@author: terri
"""

import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-10,10, num=100)
y = np.sin(x)

plt.plot(x,y, 'bo')
plt.show()