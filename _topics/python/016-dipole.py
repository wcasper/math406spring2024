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

Z = -np.log((X-1)**2+Y**2) + np.log((X+1)**2+Y**2)
U = -2*(X-1)/((X-1)**2+Y**2) + 2*(X+1)/((X+1)**2+Y**2)
V = -2*Y/((X-1)**2+Y**2) + 2*Y/((X+1)**2+Y**2)


#plt.xlabel(r'$x$')
#plt.ylabel(r'$y$')

# Normalize all gradients to focus on the direction not the magnitude
norm = np.linalg.norm(np.array((U, V)), axis=0)
U = U / norm
V = V / norm

fig, ax = plt.subplots(1, 1)
#ax.set_aspect(1)

ax.quiver(X[0:nx:3,0:ny:3], Y[0:nx:3,0:ny:3], U[0:nx:3,0:ny:3], V[0:nx:3,0:ny:3], units='xy', scale=8, color='gray', headwidth=0)
ax.contour(X, Y, Z, 100, cmap='jet', lw=2)

#plt.xticks([-L,-L/2,0,L/2,L],[r'$-L$',r'$-L/2$','0',r'$L/2$',r'$L$'])
#plt.yticks([-M,-M/2,0,M/2,M],[r'$-M$',r'$-M/2$','0',r'$M/2$',r'$M$'])


#plt.show()

plt.savefig("../fig/016-dipole.png")


