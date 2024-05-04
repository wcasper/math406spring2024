---
layout: page
title: Homework 5 Solutions
permalink: /homework/hw5-soln
---

### Directions
Solve the following problems and write up your solutions.  Your solutions should be provided in one of the following formats (in order of preference)
* typed up in $$\LaTeX$$ and submitted as a PDF on Canvas
* written legibly on blank paper, scanned into a PDF and then uploaded on Canvas
* written on ancient parchement with a quill and then flown to the instructor via owl post like in Harry Potter

If you go with the first strategy, you may wish to check out Overleaf which is a free and intuitive website for generating $$\LaTeX$$ documents online.
If you wish to use the second method and don't own a scanner at home, you can check out the numerous scanning apps available for smartphones.

You will be graded based on *completion* of all of the assigned problems, along with in-depth grading of *select* problems which will not be revealed until after the homework is graded.

**Remember:** Success in any math class is based on *practice*.  The assigned homework problems are the **bare minimum**.  You should strive to do as many problems as possible from the textbook.

# Problem 1

Find a solution of the wave equation in three dimensions

$$u_{tt} = c^2 (u_{xx} + u_{yy} + u_{zz})$$

with the initial condition

$$u(x,y,z,0) = z^3 + 4xyz + 2yx^2,\ \ u_t(x,y,z,0) = 0.$$

**Solution:**

The spherical mean of $$z^3$$ is

$$\begin{align}
\overline{z^3}
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi (z+r\cos\phi)^3 \sin\phi d\phi d\theta\\
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi (z^3+3z^2r\cos\phi + 3zr^2\cos^2\phi + r^3\cos^3\phi) \sin\phi d\phi d\theta\\
  & = \frac{1}{2}\int_0^\pi (z^3+3z^2r\cos\phi + 3zr^2\cos^2\phi + r^3\cos^3\phi) \sin\phi d\phi\\
  & = \frac{1}{2}\int_{-1}^1 (z^3+3z^2ru + 3zr^2u^2 + r^3u^3) du\\
  & = z^3 + zr^2.
\end{align}$$

The function $$4xyz$$ is harmonic, so by the Mean Value Property, it is its own spherical mean

$$\overline{xyz} = xyz.$$

Lastly, the spherical mean of 2yx^2$$ is 

$$\begin{align}
\overline{2yx^2}
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi 2(y+r\sin\phi\sin\theta)(x+r\sin\phi\cos\theta)^2 \sin\phi d\phi d\theta\\
  & = \frac{1}{2\pi}\int_0^{2\pi}\int_0^\pi x^2y\sin\phi + 2xyr\sin^2\phi\cos\theta + yr^2\sin^3\phi\cos^2\theta\\
  & + \frac{1}{2\pi}\int_0^{2\pi}\int_0^\pi x^2r\sin^2\phi\sin\theta + 2xr^2\sin^3\phi\cos\theta\sin\theta + r^3\sin^4\phi\cos^2\theta\sin\theta\\
  & = \frac{1}{2\pi}\int_0^{2\pi}\int_0^\pi x^2y\sin\phi + yr^2\sin^3\phi\cos^2\theta\\
  & = \int_0^\pi x^2y\sin\phi + \frac{1}{2}yr^2\sin^3\phi\\
  & = 2x^2y + \frac{2}{3}yr^2
\end{align}$$

Therefore

$$\overline f(x,y,z;r) = z^3 + 4xyz + 2x^2y + (z + 2y/3)r^2,$$

and also

$$\overline f_r(x,y,z;r) = 2(z + 2y/3)r.$$

This means

$$\begin{align}
u(x,y,z,t)
  & = \overline f(x,y,z;ct) + ct\overline f_r(x,y,z;ct)\\
  & = z^3 + 4xyz + 2x^2y + (z + 2y/3)c^2t^2 + 2c^2t^2(z + 2y/3)\\
  & = z^3 + 4xyz + 2x^2y + (3z + 2y)c^2t^2
\end{align}$$

# Problem 2

Find a solution $$u(x,y,t)$$ of the PDE 

$$u_{tt} = c^2(u_{xx} + u_{yy}) + a^2u$$

defined for all $$(x,y)\in\mathbb{R}^2$$ and $$t > 0$$ with the generic initial condition

$$u(x,y,0) = f(x,y),\ \ u_t(x,y,0) = g(x,y).$$

Hint: consider the function of *three* varibles $$v(x,y,z,t) = e^{az/c}u(x,y,t)$$.  Show that $$v$$ satisfies the wave equation in three dimensions.

**Solution:**

The function $$v(x,y,z,t)$$ satisfies the equation

$$\begin{align}
v_{tt}
  & = c^2(v_{xx} + v_{yy}) + a^2v\\
  & = c^2(v_{xx} + v_{yy}) + c^2v_{zz},
\end{align}$$

and therefore $$v$$ satisfies the wave equation in three dimensions, with the initial conditions

$$v(x,y,z,0) = f(x,y)e^{az/c},\quad\quad v_t(x,y,z,0) = g(x,y)e^{az/c}.$$

This means that if $$\overline f$$ and $$\overline g(

$$\begin{align}
\overline f(x,y,z;r) &= \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta)e^{a(z + r\cos\phi)/c}\sin\phi d\phi d\theta\\
\overline g(x,y,z;r) &= \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi g(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta)e^{a(z + r\cos\phi)/c}\sin\phi d\phi d\theta
\end{align}$$

then

$$v(x,y,z) = \overline f(x,y,z; ct) + ct\overline f_r(x,y,z; ct) + t\overline g(x,y,z; ct),$$

and

$$u(x,y,t) = v(x,y,0).$$

# Problem 3
Find a solution $$u(x,y,t)$$ of the PDE 

$$u_{tt} = c^2(u_{xx} + u_{yy})$$

with the initial conditions

$$u(x,y,0) = x^3 + y^3,\ \ u_t(x,y,0) = 0.$$

**Solution:**

The spherical mean of $$x^3$$ is

$$\begin{align}
\overline{x^3}
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi (x+r\sin\phi\cos\theta)^3 \sin\phi d\phi d\theta\\
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi x^3\sin\phi+3x^2r\sin^2\phi\cos\theta + 3xr^2\sin^3\phi\cos^2\theta + r^3\sin^4\phi\cos^3\theta d\phi d\theta\\
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi x^3\sin\phi+ 3xr^2\sin^3\phi\cos^2\theta d\phi d\theta\\
  & = \frac{1}{2}\int_0^\pi x^3\sin\phi+ \frac{3}{2}xr^2\sin^3\phi d\phi d\theta\\
  & = x^3 + xr^2
\end{align}$$

and the spherical mean of $$y^3$$ is 

$$\begin{align}
\overline{y^3}
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi (y+r\sin\phi\sin\theta)^3 \sin\phi d\phi d\theta\\
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi y^3\sin\phi+3y^2r\sin^2\phi\sin\theta + 3yr^2\sin^3\phi\sin^2\theta + r^3\sin^4\phi\sin^3\theta d\phi d\theta\\
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi y^3\sin\phi+ 3yr^2\sin^3\phi\sin^2\theta d\phi d\theta\\
  & = \frac{1}{2}\int_0^\pi y^3\sin\phi+ \frac{3}{2}yr^2\sin^3\phi d\phi\\
  & = y^3 + yr^2
\end{align}$$

Therefore by Kirchoff's Formula and the Method of Descent, we get the soluion

$$u(x,y,t) = x^3 + y^3 + 3(x+y)c^2t^2.$$


# Problem 4

Find a solution of the wave equation in the rectangle

$$u_{tt} = c^2(u_{xx} + u_{yy}),\ \ 0 < x < \pi,\ 0 < y < \pi$$

with homogeneous Dirichlet boundary conditions, for each of the following initial conditions

* (a) $$u(x,y,0) = x (\pi -x)y(\pi -y),\ \ u_t(x,y,0) = 0$$
* (b) $$u(x,y,0) = x (\pi -x)y,\ \ u_t(x,y,0) = 0$$

**Solution:**

* (a) The two-dimensional sine series expansion of the initial condition is 

$$x(\pi-x)y(\pi-y) = \sum_{m=1}^\infty\sum_{n=1}^\infty \frac{16(1-(-1)^m)(1-(-1)^n)}{\pi^2m^3n^3}\sin(m x)\sin(ny),$$

so the solution is

$$u(x,y,t) = \sum_{m=1}^\infty\sum_{n=1}^\infty \frac{16(1-(-1)^m)(1-(-1)^n)}{\pi^2m^3n^3}\sin(\sqrt{m^2+n^2} ct)\sin(m x)\sin(ny).$$

* (b) The two-dimensional sine series expansion of the initial condition is 

$$x(\pi-x)y = \sum_{m=1}^\infty\sum_{n=1}^\infty \frac{8(1-(-1)^m)(-1)^{n+1}}{\pi m^3n}\sin(m x)\sin(ny),$$

so the solution is

$$u(x,y,t) = \sum_{m=1}^\infty\sum_{n=1}^\infty \frac{8(1-(-1)^m)(-1)^{n+1}}{\pi m^3n}\sin(\sqrt{m^2+n^2} ct)\sin(m x)\sin(ny).$$


# Problem 5

Find a solution to the wave equation in the unit disk

$$u_{tt} = c^2\Delta u,\ \ 0 < r < 1,\ \ 0 \leq \theta < 2\pi$$

with a Dirichlet boundary condition and the initial condition

$$u(r,\theta,0) = 1-r^2,\ \ u_t(r,\theta,0) = 1.$$


**Solution:**

Since the initial condition is radially symmetric, the solution should be able to be expressed as

$$u(r,\theta,t) = \sum_{k=1}^\infty (A_k\cos(s^0_k ct) + B_k\sin(s^0_k ct))J_0(s^0_k r).$$

The coefficients themselves are determined by the $$0$$'th Fourier-Bessel series of the initial conditions.
Specifically, we calculate

$$\begin{align}
\int_0^1 J_0(s^0_kr)rdr
 & = \frac{1}{(s^0_k)^2}\int_0^{s^0_k} J_0(r)rdr \\
 & = \frac{1}{(s^0_k)^2}\int_0^{s^0_k} (J_1(r)r)'dr \\
 & = \frac{J_1(s_0^k)}{s^0_k},
\end{align}$$

and therefore

$$1 = \sum_{k=1}^\infty \frac{J_1(s_0^k)}{s^0_k} J_0(s^0_k r).$$

Likewise, we calculate

$$\begin{align}
\int_0^1 (1-r^2)J_0(s^0_kr)rdr
 & = \frac{1}{(s^0_k)^4}\int_0^{s^0_k} ((s^0_k)^2-r^2)J_0(r)rdr \\
 & = \frac{1}{(s^0_k)^4}\int_0^{s^0_k} ((s^0_k)^2-r^2)(J_1(r)r)'dr \\
 & = \frac{2}{(s^0_k)^4}\int_0^{s^0_k} J_1(r)r^2dr \\
 & = \frac{2}{(s^0_k)^4}\int_0^{s^0_k} (J_2(r)r^2)'dr \\
 & = \frac{2J_2(s^0_k)}{(s^0_k)^2},
\end{align}$$

and therefore

$$1-r^2 = \sum_{k=1}^\infty \frac{2J_2(s^0_k)}{(s^0_k)^2} J_0(s^0_k r).$$

Together, these imply

$$A_k = \frac{2J_2(s^0_k)}{(s^0_k)^2},\quad\quad B_k = \frac{J_1(s_0^k)}{(s^0_k)^2 c}$$

where we need to remember $$B_k$$ comes from the coefficients of the expansion of the initial velocity, divided by $$(s^0_k/R)c$$.

Thus our final answer is

$$u(r,\theta,t) = \sum_{k=1}^\infty \left(\frac{2J_2(s^0_k)}{(s^0_k)^2}\cos(s^0_k ct) + \frac{J_1(s_0^k)}{(s^0_k)^2 c}\sin(s^0_k ct)\right) J_0(s^0_k r).$$


