---
layout: page
title: Waves on a rectangle
---

Imagine we make a drum whose head has the shape described by domain $$\Omega\subseteq\mathbb{R}^2$$.
The height $$u(x,y,t)$$ of the drum head at position $$(x,y)\in\Omega$$ and time $$t$$ will satisfy the wave equation 

$$u_{tt} = c^2 (u_{xx} + u_{yy})$$

and typically is tightened on the rim so that it satisfies the boundary condition $$u = 0$$ on $$\partial\Omega$$.
The wave velocity $$c$$ itself is determined by factors like the tightness and material composition of the drum head.

To solve the wave equation, we use separation of variables to write

$$u(x,y,t) = \psi(x,y)\phi(t),$$

so that the equation reduces to two separate equations

$$\psi_{xx} + \psi_{yy} = -\lambda^2 \psi,$$

and

$$\phi_{tt} = -\lambda^2 c^2 \phi.$$

In particular, this shows that $$\psi(x,y)$$ will be an eigenfunction of the Laplacian on $$\Omega$$.

**Definition:** An **eigenfunction of the Laplacian** on a domain $$\Omega\subseteq\mathbb{R}^n$$ is a function $$\psi$$ which limits to zero on the boundary of $$\Omega$$ and which satisfies $$\Delta \psi = -\lambda^2 \psi$$ for inside $$\Omega$$ for some real number $$\lambda^2$$, which we call the **eigenvalue** of the Laplacian.

Thus if $$\psi$$ is an eigenfunction of the Laplacian with eigenvalue $$\lambda$$, then

$$u(x,y,t) = (A\cos(\lambda ct) + B\sin(\lambda ct))\psi(x,y)$$

is a solution of the wave equaation on the drum head with Dirichlet boundary conditions.
By taking a linear combination of these solutions, we can obtain a solutiion satisfying a desired initial condition

$$u(x,y,0) = f(x,y),\quad u_t(x,y,0) = g(x,y).$$

## Waves on a rectangle

Consider a drum head in the shape of a rectangle of length $$L$$ and width $$M$$, described by the Cartesian product $$[0,L]\times [0,M]$$.
The eigenvalues of the Laplacian on $$\Omega$$ are the values of $$\lambda$$, which are solutions of

$$\psi_{xx} + \psi_{yy} = -\lambda^2 \psi,$$

which satisfy the boundary condition

$$\psi(x,0) = 0,\ \ \psi(x,M) = 0,\ \ \psi(0,y) = 0,\ \ \psi(L,y) = 0.$$

Using separation of variables, we propose a solution of the form $$\psi(x,y) = F(x)G(y)$$, from which we get

$$F''(x)G(y) + F(x)G''(y) = -\lambda^2 F(x)G(y)$$

which results in the two equations

$$F''(x) + \mu^2 F(x) = 0,$$

$$G''(y) + (\lambda^2-\mu^2) G(y) = 0.$$

The solutions of each of these equations are given by

$$F(x) = A\cos(\mu x) + B\sin(\mu x)$$

and 

$$G(y) = C\cos( \sqrt{\lambda^2-\mu^2} y) + D\sin( \sqrt{\lambda^2-\mu^2} y).$$

Furthermore, the boundary conditions imply $$F(0) = 0$$, $$F(L) = 0$$, $$G(0) = 0$$ and $$G(M) = 0$$.
This forces $$A = 0$$ and $$C = 0$$ and also

$$\mu = m\pi /L,\ \ \ \lambda = \pi\sqrt{\frac{m^2}{L^2} + \frac{n^2}{M^2}}$$

for some integers $$m$$ and $$n$$, which without loss of generality may be taken to be positive.
In particular, the eigenvalues of the Laplacian on $$[0,L]\times [0,M]$$ look like

$$\lambda^2 = \frac{\pi^2m^2}{L^2} + \frac{\pi^2n^2}{M^2},\ \ m, n \geq 1$$

and an associated eigenfuction is

$$\psi(x,y) = \sin\left(\frac{m\pi x}{L} \right)\sin\left(\frac{n\pi y}{M}\right).$$


### Solving the wave equation on a rectangle

Now to solve the wave equation on the rectangle $$[0,L]\times [0,M]$$

$$u_{tt} = \Delta u,\ \ 0 < x < L,\ \ 0 < y < M,\ \ t > 0,$$

with a Dirichlet boundary condition and the initial condition

$$u(x,y,0) = f(x,y),\ \ u_t(x,y) = g(x,y)$$

we use a linear combination of the solutions of the form that we derived above, ie.

$$\begin{align}
u(x,y,t)
  & = \sum_{m=1}^\infty \sum_{n=1}^\infty \widetilde A_{mn} \sin(mx/L)\sin(ny/M)\cos(\omega_{m,n}ct)\\
  & + \sum_{m=1}^\infty \sum_{n=1}^\infty\widetilde B_{mn} \sin(mx/L)\sin(ny/M)\sin(\omega_{m,n} ct)
\end{align}$$

where here

$$\omega_{m,n} = \pi \sqrt{(m/L)^2+(n/M)^2}$$

for some constants $$\widetilde A_{nk}$$ and $$\widetilde B_{nk}$$.
The initial condition would then imply

$$f(x,y) = \sum_{m=0}^\infty\sum_{n=0}^\infty \widetilde A_{nk} \sin(mx/L)\sin(ny/M).$$

$$g(x,y) = \sum_{m=0}^\infty\sum_{n=0}^\infty \widetilde B_{nk} c\omega_{m,n}\sin(mx/L)\sin(ny/M).$$

To find these coefficients, we first take the sine series of the initial conditions with respect to the variable $$x$$ on $$[0,L]$$, writing

$$f(x,y) = \sum_{m=1}^\infty A_m(y)\sin(m \pi x/L),$$

and also

$$g(x,y) = \sum_{m=1}^\infty B_m(y)\sin(m \pi x/L),$$

for some functions $$A_m(y)$$ and $$B_m(y)$$.

Then for each $$m$$, we take the sine series expansions of $$A_m(y)$$ and $$B_m(y)$$ on $$[0,M]$$, ie.

$$A_m(y) = \sum_{n=1}^\infty A_{mn} \sin(n\pi y/M),\ \ \ B_m(y) = \sum_{n=1}^\infty B_{mn} \sin(n\pi y/M).$$

This allows us to write

$$f(x,y) = \sum_{m=1}^\infty \sum_{n=1}^\infty A_{mn} \sin(m\pi x/L)\sin(n\pi y/M),$$

$$g(x,y) = \sum_{m=1}^\infty \sum_{n=1}^\infty B_{mn} \sin(m\pi x/L)\sin(n\pi y/M).$$

$$A_{mn} = \frac{4}{LM}\int_0^L\int_0^M f(x,y)\sin(m\pi x/L)\sin(n\pi y/M) dydx.$$

A similar expression is true for $$B_{mn}$$.

Finally, by taking $$\widetilde A_{mn} = A_{mn}$$ and $$\widetilde B_{mn} = \frac{1}{\omega_{m,n}c} B_{mn}$$ we obtain our solution

$$\begin{align}
u(x,y,t)
  & = \sum_{m=1}^\infty \sum_{n=1}^\infty  A_{mn} \sin(mx/L)\sin(ny/M)\cos(\omega_{m,n} ct)\\
  & + \sum_{m=1}^\infty \sum_{n=1}^\infty \frac{1}{c\omega_{m,n}} B_{mn} \sin(mx/L)\sin(ny/M)\sin(\omega_{m,n} ct)
\end{align}$$


**Example:**  Consider the wave equation

$$u_{tt} = c^2(u_{xx} + u_{yy}),\ \ 0 \leq x \leq L,\ \ 0 \leq y \leq M$$

on the rectangle $$[0,L]\times [0,M]$$ with Dirichlet boundary conditions and the initial condition

$$u(x,y,0) = xy(L-x)(M-y), \ \ u_t(x,y,0) = 0.$$

We calculate

$$\begin{align}
A_{mn}
  & = \frac{4}{LM}\int_0^L\int_0^M \sin(m\pi x/L)\sin(n\pi x/M) xy(L-x)(M-y) dydx\\
  & = \frac{16L^2M^2(1-(-1)^m)(1-(-1)^n)}{\pi^6 m^3n^3},
\end{align}$$

so that our solution is 

$$
u(x,y,t)
 = \sum_{m=1}^\infty \sum_{n=1}^\infty \frac{16L^2M^2(1-(-1)^m)(1-(-1)^n)}{\pi^6 m^3n^3} \sin(mx/L)\sin(ny/M)\cos(\omega_{m,n} ct).$$

This solution is animated below, in the special case $$L=1$$, $$M=2$$, and $$c=1$$.

<video controls="" width="700" height="500" muted="" loop="" autoplay="">
<source src="python/024-wave-on-rectangle.mp4" type="video/mp4">
</video>

This solution is animated below, in the special case $$L=1$$, $$M=2$$, and $$c=1$$.

The source code for this video can be found here
* [python source code](python/024-wave-on-rectangle.py)



