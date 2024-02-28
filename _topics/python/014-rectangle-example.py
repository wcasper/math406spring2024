#!/usr/bin/python

import numpy as np

from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import animation
from matplotlib.ticker import LinearLocator


# basic parameters
nx = 50   # number of points in x dimension
ny = 50   # number of points in y dimension
L = 1
M = 2
pi = np.pi
nterms = 100


x = np.linspace(0,L,nx)
y = np.linspace(0,M,nx)
X,Y = np.meshgrid(x,y)
u = np.zeros([nx,ny])


for j in range(nx):
  for k in range(ny):
    for n in range(1,nterms+1):
      f1 = 2*(2*(-1)**n*(n*pi)**(-3) - 2*(n*pi)**(-3) - (-1)**n*(n*pi)**(-1))
      f2 = 2*(1-(-1)**n)/(n*pi)
      f3 = f1
      f4 = f2

      u[j,k] += (f1/np.sinh(n*pi*M/L))*np.sin(n*pi*x[j]/L)*np.sinh(n*pi*(M-y[k])/L)
      u[j,k] += (f2/np.sinh(n*pi*M/L))*np.sin(n*pi*x[j]/L)*np.sinh(n*pi*y[k]/L)
      u[j,k] += (f3/np.sinh(n*pi*L/M))*np.sin(n*pi*y[k]/M)*np.sinh(n*pi*(L-x[j])/M)
      u[j,k] += (f4/np.sinh(n*pi*L/M))*np.sin(n*pi*y[k]/M)*np.sinh(n*pi*x[j]/M)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
#surf = ax.plot_surface(X, Y, u, cmap=cm.coolwarm,
#                       linewidth=0, antialiased=False)




#plt.xlabel(r'$x$')
#plt.ylabel(r'$y$')
plt.xticks([0,L/2,L],['0',r'$L/2$',r'$L$'])
plt.yticks([0,M/2,M],['0',r'$M/2$',r'$M$'])

def init():
    surf = ax.plot_surface(X, Y, u, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
#    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter('{x:.02f}')
    return fig,

def animate(i):
    ax.view_init(elev=10., azim=i)
    return fig,

# Animate
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=360, interval=20, blit=True)
# Save
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])


#plt.show()

#plt.savefig("../fig/012-heat-kernel.png")


