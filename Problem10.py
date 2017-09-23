#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:59:44 2017

@author: terri
"""

import numpy as np
import matplotlib.pyplot as plt

print ('Single')
Radiusa = np.array(7000, dtype=np.float32)
Radiusb = np.array(Radiusa+ .000001, dtype=np.float32)

Volumea=4/3*np.pi*(Radiusa**3)
Volumeb=4/3*np.pi*(Radiusb**3)

d=Volumeb-Volumea

dtwo=4/3*np.pi*(Radiusb-Radiusa)*(Radiusb**2+Radiusb*Radiusa + (Radiusa**2))

h = Radiusb - Radiusa

dthree = 4 * np.pi*(Radiusa**2)*h

print ('Voulme A: ', Volumea)
print ('Voulme B: ',Volumeb)
print ('D: ',d)
print ('D2:',dtwo)
print ('H: ',h)
print ('D3: ',dthree, '\n')

Radiusa = np.array(7000, dtype=np.float64)
Radiusb = np.array(Radiusa+ .000001, dtype=np.float64)

Volumea=4/3*np.pi*(Radiusa**3)
Volumeb=4/3*np.pi*(Radiusb**3)

d=Volumeb-Volumea

dtwo=4/3*np.pi*(Radiusb-Radiusa)*(Radiusb**2+Radiusb*Radiusa + (Radiusa**2))

h = Radiusb - Radiusa

dthree = 4 * np.pi*(Radiusa**2)*h

print ('Double')
print ('Voulme A: ', Volumea)
print ('Voulme B: ',Volumeb)
print ('D: ',d)
print ('D2:',dtwo)
print ('H: ',h)
print ('D3: ',dthree, '\n')

print ('Analysis: When adding 1mm in single precision, there is no difference')
print ('because the added mm is rounded away. But when using double precision')
print('there is a difference because double holds more information than single and thus 1 mm can actually make a difference.')