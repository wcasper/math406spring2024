#!/usr/bin/python

import numpy as np
import scipy

from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import animation
from matplotlib.ticker import LinearLocator


# basic parameters
nr     = 30   # number of points in radial direction
ntheta = 30   # number of angles
nt = 600  # number of time steps
R = 1
T = 10
c = 1
pi = np.pi
nterms = 30

j0_zeros = scipy.special.jn_zeros(0,nterms)

def f(r,t):
  y = r*0;
  center = 3
  for k in range(nterms):
    A0k = 8/(R**2*(j0_zeros[k]/R)**6*scipy.special.jv(1,j0_zeros[k])**2)
    A0k *= j0_zeros[k]**4*scipy.special.jv(2,j0_zeros[k]) - 2*(j0_zeros[k]**3*scipy.special.jv(3,j0_zeros[k]))

    lamb = j0_zeros[k]/R

    y += A0k*np.cos(c*t*lamb)*scipy.special.jv(0,lamb*r)

  return y

r = np.linspace(0,R,nr)
t = np.linspace(0,T,nt)

fig, ax = plt.subplots()
ax.plot(r,1-r**4,'r--',label='initial profile')
line, = ax.plot(r, f(r,t[0]),label='u(r,t)')
plt.ylim([-2.5,2.5])
plt.xlabel("radius (r/R)")
plt.ylabel("amplitude u(r,t)")
plt.legend()

def animate(i):
    line.set_ydata(f(r,t[i]))  # update the data.
    plt.title("ct/R = %f" % t[i])
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=nt, blit=True, save_count=nt)

writer = animation.FFMpegWriter(fps=30, metadata=dict(artist='casper'), bitrate=1800)
ani.save("025-wave-on-disk-radial.mp4", writer=writer)

#plt.show()



