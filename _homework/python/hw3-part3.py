#!/usr/bin/python

import numpy as np


import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

R = 1.0000001 # radius of circle

# Create the mesh in polar coordinates and compute corresponding Z.
r = np.linspace(0, 1.0, 50)
# We have to split the angles up into different quadrants because
# *which* value for inverse tangent matters!
p1 = np.linspace(0, np.pi/2, 50)
p2 = np.linspace(np.pi/2+.0001, np.pi, 50)
p3 = np.linspace(np.pi+.0001,3*np.pi/2, 50)
p4 = np.linspace(3*np.pi/2+.0001,2*np.pi, 50)
rmat1, pmat1 = np.meshgrid(r, p1)
rmat2, pmat2 = np.meshgrid(r, p2)
rmat3, pmat3 = np.meshgrid(r, p3)
rmat4, pmat4 = np.meshgrid(r, p4)
Z1 = 2*np.arctan(((R+rmat1)/(R-rmat1))*np.tan((np.pi-pmat1)/2)) - 2*np.arctan(((R+rmat1)/(R-rmat1))*np.tan((0-pmat1)/2))
Z2 = 2*np.arctan(((R+rmat2)/(R-rmat2))*np.tan((np.pi-pmat2)/2)) - 2*np.arctan(((R+rmat2)/(R-rmat2))*np.tan((0-pmat2)/2))
Z3 = 2*np.arctan(((R+rmat3)/(R-rmat3))*np.tan((np.pi-pmat3)/2)) - 2*np.arctan(((R+rmat3)/(R-rmat3))*np.tan((0-pmat3)/2)) + 2*np.pi
Z4 = 2*np.arctan(((R+rmat4)/(R-rmat4))*np.tan((np.pi-pmat4)/2)) - 2*np.arctan(((R+rmat4)/(R-rmat4))*np.tan((0-pmat4)/2)) + 2*np.pi

Z1 = Z1/(2*np.pi)
Z2 = Z2/(2*np.pi)
Z3 = Z3/(2*np.pi)
Z4 = Z4/(2*np.pi)

# Express the mesh in the cartesian system.
X1, Y1 = rmat1*np.cos(pmat1), rmat1*np.sin(pmat1)
X2, Y2 = rmat2*np.cos(pmat2), rmat2*np.sin(pmat2)
X3, Y3 = rmat3*np.cos(pmat3), rmat3*np.sin(pmat3)
X4, Y4 = rmat4*np.cos(pmat4), rmat4*np.sin(pmat4)

# Plot the surface.
ax.plot_surface(X1, Y1, Z1, cmap=plt.cm.YlGnBu_r)
ax.plot_surface(X2, Y2, Z2, cmap=plt.cm.YlGnBu_r)
ax.plot_surface(X3, Y3, Z3, cmap=plt.cm.YlGnBu_r)
ax.plot_surface(X4, Y4, Z4, cmap=plt.cm.YlGnBu_r)

# Tweak the limits and add latex math labels.
ax.set_zlim(-0.5, 1.5)

#plt.show()
plt.savefig("hw3-part3.png")

