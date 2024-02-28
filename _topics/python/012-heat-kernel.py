#!/usr/bin/python

import numpy as np

from matplotlib import pyplot as plt


# basic parameters
nx = 100   # number of points in x dimension
kappa = 1      # diffusion coefficient

def heat_kernel(x,t):
  if t == 0:
    return 0

  return np.exp(-x*x/(4*np.pi*kappa*t))/np.sqrt(4*np.pi*t*kappa);


nx = 100
x = np.linspace(-10,10,nx)

times = [0.1,0.3,0.5,1.0]

for t in times:
  y = x*0;
  for k in range(nx):
    y[k] = heat_kernel(x[k],t)
  plt.plot(x,y,label=r"t=%0.1f$/k$" % t)

plt.ylabel(r'$K(x,t)$')
plt.xlabel(r'$x$')
plt.ylim([0,1])
plt.legend()
#plt.show()

plt.savefig("../fig/012-heat-kernel.png")


