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
xmax =  6  # maximum x value
tmax  =10  # maximum time
c = 3      # speed
pi = np.pi

# initial condition

def f(x):
  y = x*0;
  center = 3
  L = (xmax-xmin)
  for k in range(len(x)):
    xx = x[k]
    if(xx > 0):
      r = int(xx/L)
      if(r%2 == 0):
        xx = xx-r*L
      else:
        xx = xx-(r+1)*L
    if(xx < 0):
      r = int(np.abs(xx)/L)
      if(r%2 == 0):
        xx = xx+r*L
      else:
        xx = xx+(r+1)*L

    y[k] = 1-np.abs(np.abs(xx)-center)
    if(y[k] < 0):
      y[k] = 0
    if(xx < 0):
      y[k] = -y[k]

  return y

x = np.linspace(xmin,xmax,nx)
t = np.linspace(0,tmax,nx)

fig, ax = plt.subplots()
line, = ax.plot(x, f(x))
plt.ylim([-1,1])

def animate(i):
    line.set_ydata((f(x + c*t[i])+f(x - c*t[i]))/2)  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=nt, blit=True, save_count=nt)

writer = animation.FFMpegWriter(fps=30, metadata=dict(artist='casper'), bitrate=1800)
ani.save("022-wave-example3.mp4", writer=writer)

#plt.show()


