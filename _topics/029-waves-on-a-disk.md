---
layout: page
title: Waves on a disk
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

## Circular drums

Consider a drum head in the shape of a circle of radius $$R$$, described by the region $$\Omega = \{(x,y): x^2+y^2 < R^2\}$$.
The eigenvalues of the Laplacian on $$\Omega$$ are the values of $$\lambda$$, which are solutions of

$$\psi_{rr} + \frac{1}{r}\psi_r + \frac{1}{r^2}\psi_{\theta\theta} = -\lambda^2 \psi,$$

which satisfy the boundary condition $$\psi(R,\theta) = 0$$
Using separation of variables, we propose a solution of the form $$\psi(r,\theta) = F(r)G(\theta)$$, from which we get

$$F''(r)G(\theta) + \frac{1}{r}F'(r)G(\theta) + \frac{1}{r^2}F(r)G''(\theta) = -\lambda^2 F(r)G(\theta)$$

$$\frac{r^2}{F}F''(r) + \frac{r}{1}F'(r) + \frac{1}{G}G''(\theta) = -\lambda^2 r^2$$

$$r^2F''(r) + rF'(r) + (\lambda^2 r^2 + \mu^2)F(r) = 0.$$

$$G''(\theta) + \mu^2 G(\theta) = 0.$$

The solution for $$G$$ is 

$$G(\theta) = A\cos(\mu\theta) + B\sin(\mu\theta).$$

The function $$G(\theta)$$ needs to be $$2\pi$$-periodic, so $$\mu = 0,1,2,\dots$$.

The equation for $$F$$ can be converted to a standard form by letting $$F(r) = J(\lambda r)$$, giving us

$$r^2\lambda^2J''(\lambda r) + r\lambda J'(\lambda r) + (\lambda^2 r^2 + \mu^2)J(\lambda r) = 0,$$

or equivalently

$$s^2J''(s) + s J'(s) + (s^2 + \mu^2)J(s) = 0.$$

For $$\mu = n\geq 0$$ an integer, the solution $$J_n$$ of this equation which is bounded on $$(0,\infty)$$ is called a **Bessel function of the first kind**

$$J_n(s) = \sum_{m=0}^\infty \frac{(-1)^m}{m!(m+n)!}\left(\frac{x}{2}\right)^{m+n}.$$

Thus we find $$F(r) = J_n(\lambda r)$$,.
The roots of $$J_n(s)$$ are intimately connected with the the eigenvalues of the Laplacian.
In particular, suppose $$s^n_1 < s^n_2 < s^n_3 < \dots$$ are the roots.
The boundary condition $$F(R) = 0$$ implies that $$\lambda R$$ is a root of $$J_n$$, ie. $$\lambda = s^n_k/R$$ for some 

| $$s^n_k$$ |   $$n=0$$   |   $$n=1$$    |   $$n=2$$   |   $$n=3$$   |   $$n=4$$   | $$n=5$$     |
|   $$1$$   | $$3.8317$$  | $$1.8412$$   | $$3.0542$$  | $$4.2012$$  | $$5.3175$$  | $$ 6.4156$$ |
|   $$2$$   | $$7.0156$$  | $$5.3314$$   | $$6.7061$$  | $$8.0152$$  | $$9.2824$$  | $$10.5199$$ | 
|   $$3$$   | $$10.1735$$ |	$$8.5363$$   | $$9.9695$$  | $$11.3459$$ | $$12.6819$$ | $$13.9872$$ |
|   $$4$$   | $$13.3237$$ | $$11.7060$$	 | $$13.1704$$ | $$14.5858$$ | $$15.9641$$ | $$17.3128$$ |
|   $$5$$   | $$16.4706$$ | $$14.8636$$  | $$16.3475$$ | $$17.7887$$ | $$19.1960$$ | $$20.5755$$ |

The results is four two-parameter families of solutions

$$\cos(cts^n_k/R)\cos(n \theta)J_n(rs^n_k/R),\ \ \cos(cts^n_k/R)\sin(n \theta)J_n(rs^n_k/R),\ \ \sin(cts^n_k/R)\cos(n \theta)J_n(rs^n_k/R),\ \ \sin(cts^n_k/R)\sin(n \theta)J_n(rs^n_k/R).$$

### Fourier-Bessel series

The Bessel functions of the first kind prove to be a very interesting example of a collection of functions which we can express other functions in terms of.
Specifically, if we fix an integer $$n\geq 0$$, then we can write a function $$f(r)$$ on $$(0,R)$$ as

$$f(r) = \sum_{k=1}^\infty C_k J_n(s^n_k r/R)$$

for some constants $$C_1,C_2,\dots$$.
We call this expansion the $$n$$'th **Fourier-Bessel series expansion** of $$f(r)$$ in the interval $$(0,R)$$.

The value of the coefficients $$C_1, C_2, C_3,\dots$$ can be obtained from the orthogonality relation

$$\int_0^R J_n(s^n_j r/R)J_n(s^n_k r/R) rdr = \left\lbrace\begin{array}{cc} \frac{1}{2}R^2 (J_{n+1}(s^n_k))^2, & j=k\\ 0, & j\neq k\end{array}\right.$$

Using this orthogonality, we get

$$\int_0^R f(r)J_n(s^n_k r/R) rdr = C_k\frac{1}{2}R^2 (J_{n+1}(s^n_k))^2,$$

so that

$$C_k = \frac{2}{R^2} (J_{n+1}(s^n_k))^{-2} \int_0^R f(r)J_n(s^n_k r/R) rdr.$$


**Example:** Consider the function $$f(r) = R^4 - r^4$$.

To find the $$0$$'th Fourier-Bessel series expansion of $$f(r)$$ on the interval $$(0,R)$$, we will use the following property of Bessel functions

$$(x^nJ_n(x))' = x^n J_{n-1}(x).$$

Using this, we can write

$$\begin{align}
\int_0^R J_0( s^0_k r/R) (R^4-r^4)rdr
& = \frac{1}{(s^0_k/R)^{6}}\int_0^{s^0_k} J_0(x)((s^0_k)^4-x^4)xdx\\
& = \frac{1}{(s^0_k/R)^{6}}\int_0^{s^0_k} (xJ_1(x))'((s^0_k)^4-x^4)dx\\
& = \frac{4}{(s^0_k/R)^{6}}\int_0^{s^0_k} J_1(x)x^4dx\\
& = \frac{4}{(s^0_k/R)^{6}}\int_0^{s^0_k} (x^2J_2(x))'x^{2}dx\\
& = \frac{4}{(s^0_k/R)^{6}} \left((s^0_k)^4J_2(s^0_k) - 2\int_0^{s^0_k} J_2(x)x^{3}dx\right)\\
& = \frac{4}{(s^0_k/R)^{6}} \left((s^0_k)^4J_2(s^0_k) - 2\int_0^{s^0_k} (x^{3}J_3(x))'dx\right)\\
& = \frac{4}{(s^0_k/R)^{6}} \left((s^0_k)^4J_2(s^0_k) - 2((s^0_k)^{3}J_3(s^0_k))\right)
\end{align}$$

Therefore

$$R^4-r^4 = \frac{2}{R^2} \sum_{k=1}^\infty \frac{4}{(s^0_k/R)^{6}J_1(s^0_k/R)^2} \left((s^0_k)^4J_2(s^0_k) - 2((s^0_k)^{3}J_3(s^0_k))\right)J_0(s^0_k r/R).$$




### Solving the wave quation on a circular drum

Now to solve the wave equation on a circular drum of radius $$R$$

$$u_{tt} = \Delta u,\ \ 0 < r < R,\ \ 0 < \theta < 2\pi,\ \ t > 0,$$

with a Dirichlet boundary condition and the initial condition

$$u(r,\theta,0) = f(r,\theta),\ \ u_t(r,\theta) = g(r,\theta)$$

we use a linear combination of the solutions of the form that we derived above, ie.

$$\begin{align}
u(r,\theta,t)
  & = \sum_{n=0}^\infty \sum_{k=1}^\infty (\widetilde A_{nk} \cos(n\theta)+\widetilde B_{nk} \sin(n\theta))\cos( ct s_n^k/R )J_n^k(s^n_k r)\\
  & + \sum_{n=0}^\infty \sum_{k=1}^\infty (\widetilde C_{nk} \cos(n\theta)+\widetilde D_{nk} \sin(n\theta))\sin( ct s_n^k/R )J_n^k(s^n_k r).
\end{align}$$

for some constants $$\widetilde A_{nk},\widetilde B_{nk},\widetilde C_{nk},$$ and $$\widetilde D_{nk}$$ with the $$B_{0k} = D_{0k} = 0$$ for all $$k$$.
The initial condition would then imply

$$f(r,\theta) = \sum_{n=0}^\infty \sum_{k=1}^\infty (\widetilde A_{nk} \cos(n\theta)+\widetilde B_{nk} \sin(n\theta))J_n^k(s^n_k r),$$

$$g(r,\theta) = \sum_{n=0}^\infty \sum_{k=1}^\infty \frac{c s_n^k}{R}(\widetilde C_{nk} \cos(n\theta)+\widetilde D_{nk} \sin(n\theta))J_n^k(s^n_k r),$$

To find these coefficients, we first take the Fourier series of the initial conditions with respect to the variable $$\theta$$, writing

$$f(r,\theta) = A_0(r) + \sum_{n=1}^\infty A_n(r)\cos(n\theta) + B_n(r)\sin(n\theta),$$

and also

$$g(r,\theta) = C_0(r) + \sum_{n=1}^\infty C_n(r)\cos(n\theta) + D_n(r)\sin(n\theta)$$

for some functions $$A_n(r), B_n(r), C_n(r),$$ and $$D_n(r)$$.
For each $$n$$, we then take the $$n$$'th Fourier-Bessel expansions

$$A_n(r) = \sum_{k=1}^\infty A_{nk} J_n(s^n_k r),$$

$$B_n(r) = \sum_{k=1}^\infty B_{nk} J_n(s^n_k r),$$

$$C_n(r) = \sum_{k=1}^\infty C_{nk} J_n(s^n_k r),$$

$$D_n(r) = \sum_{k=1}^\infty D_{nk} J_n(s^n_k r).$$

This allows us to write

$$f(r,\theta) = \sum_{n=0}^\infty \sum_{k=1}^\infty ( A_{nk} \cos(n\theta)+ B_{nk} \sin(n\theta))J_n^k(s^n_k r),$$

$$g(r,\theta) = \sum_{n=0}^\infty \sum_{k=1}^\infty ( C_{nk} \cos(n\theta)+ D_{nk} \sin(n\theta))J_n^k(s^n_k r).$$

Finally, by taking $$\widetilde A_{nk} = A_{nk}$$, $$\widetilde B = B_{nk}$$, $$\widetilde C_{nk} = \frac{R}{cs_n^k}C_{nk}$$, and $$\widetilde D_{nk} = \frac{R}{cs_n^k}D_{nk}$$, we solve the problem.

$$\begin{align}
u(r,\theta,t)
  & = \sum_{n=0}^\infty \sum_{k=1}^\infty (A_{nk} \cos(n\theta)+ B_{nk} \sin(n\theta))\cos( ct s_n^k/R )J_n^k(s^n_k r)\\
  & + \sum_{n=0}^\infty \sum_{k=1}^\infty \frac{R}{cs_n^k}(C_{nk} \cos(n\theta)+D_{nk} \sin(n\theta))\sin( ct s_n^k/R )J_n^k(s^n_k r).
\end{align}$$

**Example:** Find a solution of the wave equation on the disk of radius $$R$$ centered at the origin with Dirichlet boundary conditions and the initial condition

$$u(r,\theta,0) = R^4-R^4,\ \ \ u_t(r,\theta,0) = 0.$$

In this case $$B_n(r) = 0$$, $$C_n(r) = 0$$, and $$D_n(r) =0$$ for all $$n$$ and $$A_n(r) = 0$$ for $$n > 0$$.
Thus we need only take the Fourier-Bessel series of $$A_0(r)$$, which we did in the previous example.  Specifically, we get

$$A_{0k} = \frac{8}{R^2(s^0_k/R)^{6}J_1(s^0_k)^2} \left((s^0_k)^4J_2(s^0_k) - 2((s^0_k)^{3}J_3(s^0_k))\right)J_0(s^0_k r/R)$$

and our solution is given by

$$u(r,\theta,t) = \sum_{k=1}^n A_{0k}\cos(ct s^0_k/R)J_0(s^0_k r/R).$$

This solution is animated below, in the special case $$R=1$$ and $$c=1$$.

<video controls="" width="700" height="500" muted="" loop="" autoplay="">
<source src="python/025-wave-on-disk.mp4" type="video/mp4">
</video>

Since this solution is radially symmetric, we can also see a nice view using a plot of the radial profile.

<video controls="" width="700" height="500" muted="" loop="" autoplay="">
<source src="python/025-wave-on-disk-radial.mp4" type="video/mp4">
</video>

The source code for these videos can be found here
* [python source code for surface plot](025-wave-on-disk.py)
* [python source code for curve plot](025-wave-on-disk-radial.py)



