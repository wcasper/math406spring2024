#!/usr/bin/python

import numpy as np

from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.patches import FancyArrowPatch


# basic parameters
nx = 100   # number of points in x dimension
ny = 100   # number of points in y dimension
L = 2
M = 2


x = np.linspace(-L,L,nx)
y = np.linspace(-M,M,ny)
X,Y = np.meshgrid(x,y)
Z = np.zeros([nx,ny])
U = np.zeros([nx,ny])
V = np.zeros([nx,ny])


for j in range(nx):
  for k in range(ny):
    Z[k,j] = -np.log((x[j]-1)**2+y[k]**2) + np.log((x[j]+1)**2+y[k]**2) 
    U[k,j] = -(x[j]-1)/((x[j]-1)**2+y[k]**2) + (x[j]+1)/((x[j]+1)**2+y[k]**2) 
    V[k,j] = -(y[k]-0)/((x[j]-1)**2+y[k]**2) + (y[k]+0)/((x[j]+1)**2+y[k]**2) 





#plt.xlabel(r'$x$')
#plt.ylabel(r'$y$')

# Normalize all gradients to focus on the direction not the magnitude
norm = np.linalg.norm(np.array((U, V)), axis=0)
U = U / norm
V = V / norm

fig, ax = plt.subplots(1, 1)
#ax.set_aspect(1)

ax.quiver(Y[0:nx:3,0:ny:3], X[0:nx:3,0:ny:3], U[0:nx:3,0:ny:3], V[0:nx:3,0:ny:3], units='xy', scale=8, color='gray', headwidth=0)
ax.contour(X, Y, Z, 100, cmap='jet', lw=2)

#plt.xticks([0,L/2,L],['0',r'$L/2$',r'$L$'])
#plt.yticks([0,M/2,M],['0',r'$M/2$',r'$M$'])


#plt.show()

plt.savefig("../fig/016-dipole.png")


