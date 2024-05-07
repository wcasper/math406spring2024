#!/usr/bin/python

import numpy as np
import scipy

from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import animation
from matplotlib.ticker import LinearLocator


# basic parameters
nx = 100  # number of points in radial direction
nt = 60   # number of time steps
xmax = 5
xmin = -xmax
tmax = 1
h0 = 1
g = 9.81
c0 = np.sqrt(g*h0)

def f(x,t):
  h = x*0

  for i in range(len(x)):
    if(x[i] < -c0*t):
      h[i] = h0;
    elif(x[i] < 2*c0*t):
      h[i] = (h0/9)*(2-x[i]/(c0*t))**2;

  return h

x = np.linspace(xmin,xmax,nx)
t = np.linspace(0,tmax,nt)

fig, ax = plt.subplots()
plt.plot(x,x*0,'r--',label='ground')
line, = ax.plot(x, f(x,t[0]),label='u(x,0)')
plt.ylim([-h0*0.1,h0*1.1])
plt.xlim([xmin,xmax])
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.legend()

def animate(i):
    line.set_ydata(f(x,t[i]))  # update the data.
    plt.title("t = %lf" % t[i])
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=nt, blit=False, save_count=nt)

writer = animation.FFMpegWriter(fps=30, metadata=dict(artist='casper'), bitrate=1800)
ani.save("031-dam-break.mp4", writer=writer)

#plt.show()



