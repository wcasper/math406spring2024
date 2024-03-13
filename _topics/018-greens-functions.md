---
layout: page
title: Green's Functions
---

The fundamental solutions of the Laplace equation in $$\mathbb{R}^n$$ are special cases of a far-reaching strategy for solving linear PDEs on specific domains, called the **method of Green's Functions**.

We start out with the definition of the Green's function for the Laplacian operator in two dimensions, followed by a more general definition.

**Definition:** Let $$\Omega\subseteq \mathbb R^2$$.  The Green's function for the Laplacian $$\Delta$$ on $$\Omega$$ is a solution $$G(x,y;s,t)$$ of

$$G_{xx}(x,y;,s,t) + G_{yy}(x,y;s,t) = \delta(x-s)\delta(y-t),\ \ (x,y)\in\Omega$$

satisfying the boundary condition that

$$G(x,y;s,t)\rightarrow 0\ \ \text{as}\ \ (x,y)\rightarrow\partial\Omega.$$

More generally, we can consider the Laplacian operator in $$n$$ dimensions, or something like the heat operator $$\partial_t - k\Delta$$ or wave operator $$\partial_t^2 - c^2\Delta$$, which are examples of **linear partial differential operators**, meaning linear transformations which are defined by partial derivatives.

**Definition:** Given a linear partial differential operator $$L$$ (such as the Laplacian operator $$L = \Delta$$) and a domain $$\Omega\subseteq \mathbb{R}^n$$, a **Green's function** for $$L$$ on $$\Omega$$ is a function $$G(\vec x;\vec t)$$ satisfying

$$LG(\vec x;\vec t) = \delta(\vec x-\vec t),$$

with the boundary condition that

$$G(x,y;s,t)\rightarrow 0\ \ \text{as}\ \ (x,y)\rightarrow\partial\Omega.$$

Here $$\vec x = (x_1,\dots, x_n)$$ and $$\vec t = (t_1,\dots, t_n)$$ and the operator $$L$$ is acting on $$\vec x$$, treating $$t_1,\dots, t_n$$ as parameters.

The utility of Green's functions comes from the observation that if

$$u(\vec x) = \int_{\Omega} G(\vec x;\vec t) f(\vec t)dt,$$

then

$$Lu(\vec x) = \int_{\Omega} LG(\vec x;\vec t) f(\vec t)d\vec t = \int_{\Omega} \delta(\vec x-\vec t) f(\vec t)d\vec t = f(\vec x).$$

Thus $$u(\vec x)$$ satisfies

$$Lu = f(\vec x),\ \ \text{with}\ \ u(\vec x)\rightarrow 0\ \ \text{as}\ \ \vec x\rightarrow\partial \Omega.$$

**Example:**  Consider the one dimensional boundary value problem

$$y'' -y = f(x),\ \ y(\pi/2) = 0,\ y(\pi) = 0.$$

To solve this, we look for the Green's function $$G(x;t)$$ which satisfies

$$G''(x;t) - G(x;t) = \delta(x-t).$$

Taking the Fourier transform, we obtain

$$-4\pi^2 \xi^2 \hat G(\xi;t) -  \hat G(\xi;t) = e^{-2\pi i \xi t}.$$

This says

$$\hat G(\xi;t) = \frac{-1}{1 + 4\pi^2\xi^2}e^{-2\pi i \xi t}$$

and therefore

$$G(x;t) = -\frac{1}{2}e^{-\lvert (x+t)\rvert}.$$

To achieve the boundary condition, we can add on any solution of the homogeneous equation $$y''-y=0$$.
To get $$G(\pm \pi;t) = 0$$, we thus obtain

$$G(x;t) = -\frac{1}{2}e^{-\lvert (x+t)\rvert} - \frac{1}{2}e^{-\lvert (\pi+t)\rvert}\cosh(x)+\frac{1}{2}e^{-\lvert (\pi/2+t)\rvert}\sinh(x).$$

**Example:**  Consider Poisson's equation on the disk $$\Omega = D_R(0,0)$$

$$u_{xx} + u_{yy} = \rho(x,y),\ \ (x,y)\in D_R(0,0).$$

The Green's function for this equation satisfies

$$G_{xx}(x,y;s,t) + G_{yy}(x,y;s,t) = \delta(x-s,y-t),\ \ (x,y)\in D_R(0,0).$$

A solution of this equation is

$$G(x,y;s,t) = \frac{1}{2\pi}\ln \sqrt{(x-s)^2+(y-t)^2} + H(x,y;s,t)$$

for any function $$H$$ which is harmonic on $$D_R(0,0)$$.

Consider the point $$(s^*,t^*) = c(s,t)$$ for $$c = R^2/(s^2+t^2)$$, called the **Schwarz reflection** of $$(s,t)$$.
Then for any $$(x,y)\in\partial D_R(0,0)$$ 

$$\sqrt{(x-s^*)^2+(y-t^*)^2} = \sqrt{R^2-2c(xs+yt) + c^2(s^2+t^2)} = \frac{R}{\sqrt{s^2+t^2}}\sqrt{(s-x)^2+(y-t)^2}.$$

It follows that

$$H(x,y;s,t) = -\frac{1}{2\pi}\ln \sqrt{(x-s^*)^2+(y-t^*)^2} + \frac{1}{2\pi} \ln \frac{R}{\sqrt{s^2+t^2}}$$

is harmonic on $$D_R(0,0)$$ and makes $$G(x,y;s,t)$$ vanish on $$\partial D_R(0,0)$$.

Thus the Green's function is

$$G(x,y;s,t) = \frac{1}{2\pi}\ln \frac{\sqrt{(x-s)^2+(y-t)^2}}{R} - \frac{1}{2\pi}\ln \frac{\sqrt{(x-s^*)^2+(y-t^*)^2}}{R}+ \frac{1}{2\pi} \ln \frac{R}{\sqrt{s^2+t^2}}.$$

**Example:**  The Green's function for Poisson's equation on the upper half plane $$\mathbb H = \{(x,y): y>0\}$$ is given by

$$G(x,y;s,t) = \frac{1}{4\pi}\ln \frac{(x-s)^2+(y-t)^2}{(x-s)^2+(y+t)^2}.$$






