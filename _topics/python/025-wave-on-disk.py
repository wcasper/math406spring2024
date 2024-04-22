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

r = np.linspace(0,R,nr)
theta = np.linspace(0,2*pi,ntheta)
t = np.linspace(0,T,nt)
rarray,Theta = np.meshgrid(r,theta)
X = rarray*np.cos(Theta)
Y = rarray*np.sin(Theta)
u = np.zeros([nr,ntheta,nt])

j0_zeros = scipy.special.jn_zeros(0,nterms)

for ti in range(nt):
  for k in range(1,nterms+1):
    A0k = 8/(R**2*(j0_zeros[k-1]/R)**6*scipy.special.jv(1,j0_zeros[k-1])**2)
    A0k *= j0_zeros[k-1]**4*scipy.special.jv(2,j0_zeros[k-1]) - 2*(j0_zeros[k-1]**3*scipy.special.jv(3,j0_zeros[k-1]))

    lamb = j0_zeros[k-1]/R

    u[:,:,ti] += A0k*np.cos(c*t[ti]*lamb)*scipy.special.jv(0,lamb*rarray)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X, Y, u[:,:,0], cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)



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
  ax.set_zlim(-1, 1)

  return fig,

# Animate
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=nt, interval=20, blit=True)
# Save
anim.save('025-wave-on-disk.mp4', fps=30, extra_args=['-vcodec', 'libx264'])


plt.show()


