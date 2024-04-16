---
layout: page
title: Method of descent
---

To solve the wave equation in two dimesions without boundary conditions, we rely on the fact that Kirchhoff's Formula in three dimensions gives us a beautifully simple solution.
Then if we have a two dimensional problem

$$u_{tt} = c^2(u_{xx} + u_{yy})$$

with the initial conditions

$$u(x,y,0) = f(x,y),\ \ u_t(x,y,0) = g(x,y)$$

we can turn it into a three-dimensional wave problem by extending the initial value problem constantly in the $$z$$-direction.
Thus we introduce a new function $$\widetilde u(x,y,z,t)$$ which is a solution of

$$\widetilde u_{tt} = c^2(\widetilde u_{xx} + \widetilde u_{yy} + \widetilde u_{zz})$$

$$\widetilde u(x,y,z,0) = f(x,y),\ \ \widetilde u_t(x,y,z,0) = g(x,y)$$

Then from Kirchhoff's Formula, the solution of this three-dimensional equation is

$$\widetilde u(x,y,z,t) = \overline f(x,y,z;ct) + ct\overline f_r(x,y,z;ct) + t\overline g(x,y,z;ct),$$

where here $$\overline f$$ and $$\overline g$$ are the spherical means

$$\begin{align}
f(x,y,z;r)
  & = \frac{1}{4\pi} \int_0^{2\pi}\int_0^\pi f(x + r\sin\phi\cos\theta, y + r\sin\phi\sin\theta) \sin\phi d\phi d\theta\\
  & = \frac{1}{2\pi} \int_0^{2\pi}\int_0^{\pi/2} f(x + r\sin\phi\cos\theta, y + r\sin\phi\sin\theta) \sin\phi d\phi d\theta\\
  & = \frac{1}{2\pi r} \int_0^{2\pi}\int_0^{r} f(x + \rho\cos\theta, y + \rho\sin\theta) \frac{\rho}{\sqrt{r^2-\rho^2}} d\rho d\theta.
\end{align}$$

This can be viewed as a two-dimensional integral over the disk of radius $$r$$ centered at $$(x,y)$$, ie.

$$f(x,y,z;r) = \frac{1}{2\pi r} \iint_{D_r(x,y)} \frac{f(x',y')}{\sqrt{r^2-(x'-x)^2-(y'-y)^2}} dA'.$$

Likewise,

$$g(x,y,z;r)  = \frac{1}{2\pi r} \iint_{D_r(x,y)} \frac{f(x',y')}{\sqrt{r^2-(x'-x)^2-(y'-y)^2}} dA'.$$

The derivative with respect to $$r$$ has the formula

$$f_r(x,y,z;r) = \frac{1}{2\pi r} \iint_{D_r(x,y)} \frac{\nabla f(x',y')\cdot \langle x'-x,y'-y\rangle}{\sqrt{r^2-(x'-x)^2-(y'-y)^2}} dA'.$$

All of these are *independent* of the value of $$z$$, so the solution the two-dimensional problem is

$$u(x,y,t) = \overline f(x,y,0;ct) + ct\overline f_r(x,y,0;ct) + t\overline g(x,y,0;ct),$$

which we can rewrite as

$$u(x,y;t) = \frac{1}{2\pi ct} \iint_{D_r(x,y)} \frac{f(x',y') + \nabla f(x',y')\cdot \langle x'-x,y'-y\rangle + tg(x',y')}{\sqrt{c^2t^2-(x'-x)^2-(y'-y)^2}} dA'.$$

This is called Poisson's formula for the wave equation.
Moreover, the strategy of solving the differential equation in three dimensions and then restricting it to two dimensions is called Hadamard's **method of descent**.

**Example:**  Find a solution of the initial value problem 

$$u_{tt} = c^2(u_{xx} + u_{yy})$$

with the initial conditions

$$u(x,y,0) = x^2(x+y),\ \ u_t(x,y,0) = 0.$$




