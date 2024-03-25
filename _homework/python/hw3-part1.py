#!/usr/bin/python

import numpy as np

from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import animation
from matplotlib.ticker import LinearLocator


# basic parameters
nx = 100   # number of points in x dimension
ny = 100   # number of points in x dimension
itmax = 50 # maximum number of iterations
L = 3
M = 2
pi = np.pi

x = np.linspace(0,L,nx)
y = np.linspace(0,M,ny)
X,Y = np.meshgrid(x,y)
Z = X*0;

for n in range(1,itmax):
  coeff = 4*(1-(-1)**n)/((n*pi)**3)
  Z += coeff*(L*L/np.sinh(n*pi*M/L))*np.sin(n*pi*X/L)*np.sinh(n*pi*(M-Y)/L)
  Z += coeff*(L*L/np.sinh(n*pi*M/L))*np.sin(n*pi*X/L)*np.sinh(n*pi*Y/L)
  Z += coeff*(M*M/np.sinh(n*pi*L/M))*np.sin(n*pi*Y/M)*np.sinh(n*pi*(L-X)/M)
  Z += coeff*(M*M/np.sinh(n*pi*L/M))*np.sin(n*pi*Y/M)*np.sinh(n*pi*X/M)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface');

#plt.show()
plt.savefig("hw3-part1.png")

