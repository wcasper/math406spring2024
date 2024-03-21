#!/usr/bin/python

import numpy as np

from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import animation
from matplotlib.ticker import LinearLocator


# basic parameters
nx = 200   # number of points in x dimension
nt = 100   # number of time steps
xmin =  0  # minimum x value
xmax =  9  # maximum x value
tmax  = 3  # maximum time
c = 5      # speed
pi = np.pi

# initial condition

def f(x):
  y = x*0;
  center = 3
  for k in range(len(x)):
    y[k] = 1-np.abs(np.abs(x[k])-center)
    if(y[k] < 0):
      y[k] = 0
    if(x[k] < 0):
      y[k] = -y[k]

  return y

x = np.linspace(xmin,xmax,nx)
t = np.linspace(0,tmax,nx)

fig, ax = plt.subplots()
line, = ax.plot(x, f(x))
plt.ylim([-1/2,1])

def animate(i):
    line.set_ydata((f(x + c*t[i])+f(x - c*t[i]))/2)  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=nt, blit=True, save_count=nt)

writer = animation.FFMpegWriter(fps=30, metadata=dict(artist='casper'), bitrate=1800)
ani.save("022-wave-example2.mp4", writer=writer)

#plt.show()


