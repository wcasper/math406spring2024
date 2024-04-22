#!/usr/bin/python

import numpy as np

from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import animation
from matplotlib.ticker import LinearLocator


# basic parameters
nx = 30   # number of points in x dimension
ny = 30   # number of points in y dimension
nt = 600  # number of time steps
L = 1
M = 2
T = 10
c = 1
pi = np.pi
nterms = 10

x = np.linspace(0,L,nx)
y = np.linspace(0,M,nx)
t = np.linspace(0,T,nt)
X,Y = np.meshgrid(x,y)
u = np.zeros([nx,ny,nt])

for ti in range(nt):
  for m in range(1,nterms+1):
    for n in range(1,nterms+1):
      Amn = 16*L**2*M**2*(1-(-1)**m)*(1-(-1)**n)/(pi**6*m**3*n**3)
      lamb = pi*np.sqrt((m/L)**2 + (n/M)**2)

      u[:,:,ti] += Amn*np.sin(m*pi*X/L)*np.sin(n*pi*Y/M)*np.cos(lamb*c*t[ti])

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X, Y, u[:,:,0], cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)




#plt.xlabel(r'$x$')
#plt.ylabel(r'$y$')
plt.xticks([0,L/2,L],['0',r'$L/2$',r'$L$'])
plt.yticks([0,M/2,M],['0',r'$M/2$',r'$M$'])

def init():
    surf = ax.plot_surface(X, Y, u[:,:,0], cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
#    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter('{x:.02f}')
    return fig,

def animate(i):
  ax.cla()
  ax.plot_surface(X, Y, u[:,:,i], cmap=cm.coolwarm,
                  linewidth=0, antialiased=False)
  ax.set_zlim(-0.2, 0.2)

  return fig,

# Animate
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=nt, interval=20, blit=True)
# Save
anim.save('024-wave-on-rectangle.mp4', fps=30, extra_args=['-vcodec', 'libx264'])


plt.show()

#plt.savefig("../fig/012-heat-kernel.png")

