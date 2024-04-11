---
layout: page
title: Kirchhoff's formula
---

The method of spherical means tells us that 

$$\overline u(x,y,z,t;r) = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi u(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi,t)\sin\phi d\phi d\theta$$

satisfies

$$\overline u_{tt} = c^2(\overline u_{rr} + \frac{2}{r}\overline u_r).$$

In other words, the spherical means behave like radially symmetric spherical waves.
In particular $$r\overline u$$ satisfies the one-dimensional wave equation on the half-line $$0 < r < \infty$$, and its solution must be given by

$$\overline u(x,y,z,t;r) = \frac{1}{2r} ((r+ct)\overline f(x,y,z;r+ct) + \lvert r-ct\rvert\overline f(x,y,z;\lvert r-ct\rvert)) + \frac{1}{2rc}\int_{\lvert r-ct\rvert}^{r+ct}s\overline g(x,y,z;s)ds.$$

The solution of the wave equation is given by taking the limit as $$r\rightarrow 0+$$.
In taking this limit, without loss of generality, we may assume $$0 < r < ct$$, so that $$\lvert r-ct\rvert = -r+ct$$.

By the definition of the derivative

$$\lim_{r\rightarrow 0+} \frac{1}{2r} ((r+ct)\overline f(x,y,z;r+ct) + (-r+ct)\overline f(x,y,z;-r+ct)) = \overline f(x,y,z; ct) + ct\overline f_r(x,y,z; ct).$$

Also, by the Fundamental Theorem of Calculus

$$\lim_{r\rightarrow 0+} \frac{1}{2rc}\int_{-r+ct}^{r+ct}s\overline g(x,y,z;s)ds = t \overline g(x,y,z;ct).$$

This leads to a strikingly beautiful formula for the solution of the wave equation in three dimensions, called Kirchhoff's formula.

**Theorem (Kirchhoff's Formula):**  The solution of the wave equation on $$\mathbb R^3$$ with the initial condition

$$u(x,y,z,0) = f(x,y,z),\ \ \text{and}\ \ u_t(x,y,z,0) = g(x,y,z)$$

is given by

$$u(x,y,z,t) = \overline f(x,y,z; ct) + ct\overline f_r(x,y,z; ct) + t\overline g(x,y,z; ct).$$


## Example application

As an example, we will solve the wave equation on $$\mathbb R^3$$ with the initial condition

$$u(x,y,z,0) = x^3+y^2z,\ \ u_t(x,y,z,0) = 0.$$

**Solution:**

We calculate 

$$\overline f(x,y,z,r)  = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi [(x + r\sin\phi\cos\theta)^3 + (y + r\sin\phi\sin\theta)^2(z + r\cos\phi)]  \sin\phi d\phi d\theta.$$

It make sense to break this up into two parts.

$$\begin{align}
\overline{x^3}
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi (x + r\sin\phi\cos\theta)^3\sin\phi\\
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi x^3\sin\phi + 3x^2r\sin^2\phi\cos\theta + 3xr^2\sin^3\phi\cos^2\theta + r^3\sin^4\phi\cos^3\theta d\phi d\theta\\
  & = \frac{1}{4\pi}\int_0^{2\pi} 2x^3  + \frac{3\pi}{2}x^2r\cos\theta + 4xr^2\cos^2\theta + \frac{3\pi}{8} r^3 \cos^3\theta d\theta\\
  & = \frac{1}{4\pi} (4\pi x^3  + 0 + 4\pi xr^2 + 0) = x^3 + xr^2.
\end{align}$$

$$\begin{align}
\overline{y^2z}
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi (y + r\sin\phi\sin\theta)^2(z + r\cos\phi)\sin\phi\\
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi y^2z\sin\phi + 2yrz\sin^2\phi\sin\theta + r^2z\sin^3\phi\sin^2\theta d\phi d\theta\\
  & + \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi y^2r\sin\phi\cos\phi + 2yr^2\sin^2\phi\cos\phi\sin\theta + r^3\sin^3\phi\cos\phi\sin^2\theta d\phi d\theta\\
  & = \frac{1}{4\pi}\int_0^{2\pi} 2y^2z + \pi yrz\sin\theta + \frac{4}{3}r^2z\sin^2\theta d\theta\\
  & = \frac{1}{4\pi}( 4\pi y^2z + 0 + \frac{4\pi}{3}r^2z) = y^2z + \frac{1}{3}r^2z.
\end{align}$$

Thus

$$\overline f(x,y,z,r) = x^3 + y^2z + (x + z/3)r^2,$$

and

$$\overline f_r(x,y,z,r) = 2(x + z/3)r,$$

and by Kirchhoff's Formula

$$\begin{align}
u(x,y,z,t)
  & = \overline f(x,y,z,ct) + ct\overline f_r(x,y,z,ct) = (x^3 + y^2z + 2(x + z/3)ct\\
  & = x^3 + y^2z + (x + z/3)c^2t^2 + ct(2(x + z/3)ct)\\
  & = x^3 + y^2z + (3x + z)c^2t^2
\end{align}$$

One can now double-check $$u_{tt} = 2c^2(3x+z)$$ and $$\Delta u = 6x + 2z$$, so that $$u_{tt} = c^2u_{xx}$$.




