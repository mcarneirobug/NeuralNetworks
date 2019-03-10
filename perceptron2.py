# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:00:39 2019

@author: Matheus
"""

import numpy as np

entrada = np.array([1, 7, 5])
pesos   = np.array([0.8, 0.1, 0])

def soma(e, p):
    return e.dot(p)
#dot product / produto escalar
    
    
s = soma(entrada, pesos)

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

r = stepFunction(s)