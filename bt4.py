#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 13:17:49 2022

@author: kartik
"""

ph0 = 0.8
ph1 = 0.2
mu=500
sigma_sq_0 = 1
sigma_sq_1 = 0.35
sse = 4.2
n= 10

import numpy as np
def pdf(sigma_sq,sse):
  prob = pow(1/np.sqrt(2*np.pi*sigma_sq),n) * np.exp(-0.5*sse/sigma_sq)
  return prob

probh0 = pdf(sigma_sq_0,sse)
probh1 = pdf(sigma_sq_1,sse)

ph0_y=(ph0*probh0)/(ph0*probh0+ph1*probh1) ##P(H0|y)
print(ph0_y)

bayes_f = (probh0/probh1)/(ph0/ph1)
print(bayes_f)