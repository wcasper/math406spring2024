#!/usr/bin/python

import numpy as np

from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import animation
from matplotlib.ticker import LinearLocator


# basic parameters
nx = 200   # number of points in x dimension
L = 6
pi = np.pi

nvals = [25,50,75,100]
ntest = len(nvals)

x = np.linspace(0,L,nx)
u = np.zeros([nx,ntest])

for i in range(ntest):
  u[:,i] = 0.5
  for n in range(1,nvals[i]):
    u[:,i] += (-2/(n*pi))*np.sin(n*pi/2)*np.cos(n*pi*x/L)

  plt.plot(x,u[:,i],label='N=%i iter' % nvals[i])

plt.legend()
plt.savefig('hw1-part3.png')


