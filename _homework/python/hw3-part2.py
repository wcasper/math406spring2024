#!/usr/bin/python

import numpy as np


import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

R = 1 # radius of circle

# Create the mesh in polar coordinates and compute corresponding Z.
r = np.linspace(0, 1.25, 50)
p = np.linspace(0, 2*np.pi, 50)
rmat, pmat = np.meshgrid(r, p)
Z = 1 + (3/R)*rmat*np.sin(pmat) - (5/R**2)*rmat*rmat*np.cos(2*pmat)

# Express the mesh in the cartesian system.
X, Y = rmat*np.cos(pmat), rmat*np.sin(pmat)

# Plot the surface.
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)

# Tweak the limits and add latex math labels.
ax.set_zlim(-10, 15)

#plt.show()
plt.savefig("hw3-part2.png")

