---
layout: page
title: Method of Spherical Means
---

To solve the wave equation in higher dimensions, we rely on deep insights by the physicists Huygens and Fresnel, who realized that waves in three dimensions can always be represented as superpositions of waves coming from (potentially many) basic spherically symmetric waves, centered at various points.


## Spherically symmetric waves

To start, let's try to understand what a solution to the wave equation with a spherically symmetric initial condition might look like in three dimensional space.
A spherically symmetric initial condition will be one which does not depend on the spherical angles $$\theta$$ and $$\phi$$, so it will look something like

$$u(\rho,\theta,\phi,t) = f(\rho),\ \ u_t(\rho,\theta,\phi,t) = g(\rho).$$

By symmetry, we would expect that there would be no differences between the values of the function as we change the spherical angle.  In other words, we would expect that the wave equation in spherical coordinates

$$u_{tt} = c^2\left(u_{\rho\rho} + \frac{2}{\rho}u_\rho + \frac{1}{\rho^2\sin^2\phi}u_{\theta\theta} + \frac{1}{\rho^2}u_{\phi\phi}+\frac{\cot(\phi)}{\rho^2}u_\phi\right)$$

will reduce to the equation

$$u_{tt} = c^2\left(u_{\rho\rho} + \frac{2}{\rho}u_\rho\right)$$

because the derivatives with respect to the spherical angles will be zero.
In particular, the solution will actually be a function of only the variables $$\rho$$ and $$t$$, ie. $$u(\rho,\theta,\phi,t)$$ 
Now to solve this, we define $$v(\rho,t) = \rho u(\rho,t)$$.
Substituting this in, th equation becomes

$$v_{tt} = c^2v_{\rho\rho}, v(\rho,0) = \rho f(\rho),\ v_t(\rho,0) = \rho g(\rho)$$

so that $$v(\rho,t)$$ is a solution of the wave equation on the half-line $$(0,\infty)$$!
Using d'Alembert's formula and the reflection method, we find the solution to be

$$v(\rho,t) = \frac{1}{2}((\rho+ct)f(\rho+ct) + (\rho-ct)f(\lvert \rho-ct \rvert)) + \frac{1}{2c}\int_{\lvert \rho-ct \rvert}^{\rho+ct} sg(s)ds.$$

Thus a spherically symmetric wave will look like

$$u(\rho,t) = \frac{1}{2\rho}((\rho+ct)f(\rho+ct) + (\rho-ct)f(\rho-ct)) + \frac{1}{2\rho c}\int_{\rho-ct}^{\rho+ct} sg(s)ds.$$


## Method of spherical means

So far, we've managed to solve the wave equation in three dimension, provided that the initial condition is spherically symmetric around the origin.
In fact, since translating a solution of the wave equation gives us another solution of the wave equation, we can actually solve the wave equation for initial conditions that are spherically symmetric around a point other than the origin.

To solve the wave equation with a more general initial condition is more difficult.

We rely instead on the idea of *spherical means*.

**Definition:**  The **spherical mean** of radius $$r$$ of a function $$f(x,y,z)$$ at the point $$(x,y,z)$$ is the average value of the function $$f$$ over the surface of a sphere of radius $$r$$ centered at $$(x,y,z)$$

$$\overline f(x,y,z;r) = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\sin\phi d\phi d\theta.$$

Importantly, notice that when $$f$$ is continuous

$$\begin{align}
\lim_{r\rightarrow 0+} \overline f(x,y,z;r)
  & = \lim_{r\rightarrow 0+}\frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\sin\phi d\phi d\theta\\
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi \lim_{r\rightarrow 0+}f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\sin\phi d\phi d\theta\\
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi f(x,y,z)\sin\phi d\phi d\theta = f(x,y,z).
\end{align}$$

Therefore the value of a function $$f(x,y,z)$$ can be recovered from its spherical means.

We first establish an important lemma about spherical means.

**Lemma:**  Suppose that $$f$$ is a twice continuously differentiable function in a domain containing the closure of the ball $$B_r(x,y,z)$$.  Then

$$\frac{\partial}{\partial r} \overline f(x,y,z;r) = \frac{1}{4\pi r^2}\int_{B_r(x,y,z)} \Delta f dV.$$

**Proof:**

From the chain rule,

$$\begin{align}
\frac{\partial}{\partial r} f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)
& = f_x(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\frac{\partial}{\partial r} (x + r\sin\phi\cos\theta)\\
& + f_y(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\frac{\partial}{\partial r} (y + r\sin\phi\sin\theta)\\
& + f_z(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\frac{\partial}{\partial r} (z + r\cos\phi)\\
& = \nabla f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi) \cdot \hat n(\theta,\phi),
\end{align}$$

where here

$$\hat n(\theta,\phi) = \langle \sin\phi\cos\theta,\sin\phi\sin\theta,\cos\phi\rangle$$

is the unit normal vector on the surface of the sphere.  Thus by the divergence theorem

$$\begin{align}
\frac{\partial}{\partial r} \overline f(x,y,z;r)
  & \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi \frac{\partial}{\partial r}f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\sin\phi d\phi d\theta\\
  & \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi  \nabla f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\cdot\hat n(\theta,\phi)\sin\phi d\phi d\theta\\
  & \frac{1}{4\pi r^2}\int_0^{2\pi}\int_0^\pi \nabla f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\cdot\hat n(\theta,\phi) r^2\sin\phi d\phi d\theta\\
  & \frac{1}{4\pi r^2}\iint_{\partial B_r(x,y,z)}  \nabla f\cdot \hat n dS\\
  & \frac{1}{4\pi r^2}\iiint_{B_r(x,y,z)} \Delta f dS
\end{align}$$

:black_square_button:

We also require a second lemma relating surface integrals over the sphere to volume integrals.

**Lemma:**  Suppose that $$h$$ is a continuous function in a domain containing the closure of the ball $$B_r(x,y,z)$$.  Then

$$\frac{\partial}{\partial r}\iiint_{B_r(x,y,z)} h dV = \iint_{\partial B(x,y,z)} h dS.$$

**Proof:**

By the Fundamental Theorem of Calculus

$$\begin{align}
\frac{\partial}{\partial r} \iiint_{B_r(x,y,z)} h dV 
 & = \frac{\partial}{\partial r} \int_0^{2\pi}\int_0^\pi \int_0^r h(x+\rho\sin\phi\cos\theta,y+\rho\sin\phi\sin\theta,z+\rho\cos\phi) \rho^2\sin\phi d\rho d\theta d\phi\\
 & = \int_0^{2\pi}\int_0^\pi h(x+r\sin\phi\cos\theta,y+ r\sin\phi\sin\theta,z+ r\cos\phi) r^2\sin\phi d\rho d\theta d\phi\\
 & = \iint_{\partial B(x,y,z)} h dS.
\end{align}$$

:black_square_button:

Now suppose that $$u$$ is a solution of the wave equation on a domain $$\Omega$$ containing the closure of a ball $$B_r(x,y,z)$$.
Then its spherical mean

$$\overline u(x,y,z,t;r) = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi u(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi,t)\sin\phi d\phi d\theta$$

satisfies

$$u_r(x,y,z,t;r) = \frac{1}{4\pi r^2}\iiint_{B_r(x,y,z)} \Delta u dV = \frac{1}{4\pi r^2c^2}\iiint_{B_r(x,y,z)} u_{tt} dV$$

by the first Lemma.  Therefore the second Lemma tells us

$$\begin{align}
\frac{\partial}{\partial r}(r^2\overline u_r(x,y,z,t;r))
  & = \frac{1}{4\pi c^2}\frac{\partial}{\partial r}\iiint_{B_r(x,y,z)} u_{tt} dV\\
  & = \frac{1}{4\pi c^2}\iint_{\partial B_r(x,y,z)} u_{tt} dV\\
  & = \frac{\partial^2}{\partial t^2}\frac{1}{4\pi c^2}\iint_{\partial B_r(x,y,z)} u dV\\
  & =\frac{r^2}{c^2} \overline u_{tt}(x,y,z,t;r)
\end{align}$$

Then since

$$\frac{\partial}{\partial r}(r^2\overline u_r(x,y,z,t;r)) = r^2\overline u_{rr}(x,y,z,t;r) + 2r\overline u_r(x,y,z,t;r)$$

this says

$$r^2\overline u_{rr} + 2r\overline u_r = \frac{r^2}{c^2} \overline u_{tt}.$$

we obtain the following amazing result, which says that the spherical average of a wave at a point itself evolves like a spherically symmetric wave!

**Theorem (Method of Spherical Means):**  Suppose that $$u(x,y,z;t)$$ is a solution of the wave equation in $$\mathbb{R}^3$$ with the initial condition $$u(x,y,z,0) = f(x,y,z)$$ and $$u_t(x,y,z,0) = g(x,y,z)$$.  Then the spherical means satisfy

$$\overline u_{tt} = c^2(\overline u_{rr} + \frac{2}{r}\overline u_r).$$

Consequently, the spherical means are given by the equation

$$\overline u(x,y,z,t;r) = \frac{1}{2r} ((r+ct)\overline f(x,y,z;r+ct) + (r-ct)\overline f(x,y,z;\lvert r-ct\rvert)) + \frac{1}{2rc}\int_{\lvert r-ct\rvert}^{r+ct}s\overline g(x,y,z;s)ds.$$

The solution of the wave equation is given by taking the limit as $$r\rightarrow 0+$$.
In taking this limit, without loss of generality, we may assume $$0 < r < ct$$, so that $$\lvert r-ct\rvert = -r+ct$$.

By the definition of the derivative

$$\lim_{r\rightarrow 0+} \frac{1}{2r} ((r+ct)\overline f(x,y,z;r+ct) + (r-ct)\overline f(x,y,z;-r+ct)) = \overline f(x,y,z; ct) + ct\overline f_r(x,y,z; ct).$$

Also, by the Fundamental Theorem of Calculus

$$\lim_{r\rightarrow 0+} \frac{1}{2rc}\int_{-r+ct}^{r+ct}s\overline g(x,y,z;s)ds = t \overline g(x,y,z;ct).$$

This leads to a strikingly beautiful formula for the solution of the wave equation in three dimensions, called Kirchhoff's formula.

**Theorem (Kirchhoff's Formula):**  The solution of the wave equation on $$\mathbb R^3$$ with the initial condition

$$u(x,y,z,0) = f(x,y,z),\ \ \text{and}\ \ u_t(x,y,z,0) = g(x,y,z)$$

is given by

$$u(x,y,z,t) = \overline f(x,y,z; ct) + ct\overline f_r(x,y,z; ct) + t\overline g(x,y,z; ct).$$

**Example:** Solve the wave equation on $$\mathbb R^3$$ with the initial condition

$$u(x,y,z,0) = x^3+y^2z,\ \ u_t(x,y,z,0) = 0.$$

**Solution:**

We calculate 

$$\overline f(x,y,z,r)  = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi [(x + r\sin\phi\cos\theta)^3 + (y + r\sin\phi\sin\theta)^2(z + r\cos\phi)]  \sin\phi d\phi d\theta.$$

It make sense to break this up into two parts.

$$\begin{align}
\frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi (x + r\sin\phi\cos\theta)^3\sin\phi
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi x^3\sin\phi + 3x^2r\sin^2\phi\cos\theta + 3xr^2\sin^3\phi\cos^2\theta + r^3\sin^4\phi\cos^3\theta d\phi d\theta\\
  & = \frac{1}{4\pi}\int_0^{2\pi} 2x^3  + \frac{3\pi}{2}x^2r\cos\theta + 4xr^2\cos^2\theta + \frac{3\pi}{8} r^3 \cos^3\theta d\theta\\
  & = \frac{1}{4\pi} (4\pix^3  + 0 + 4\pi xr^2 + 0) = x^3 + xr^2.
\end{align}$$

$$\begin{align}
\frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi (y + r\sin\phi\sin\theta)^2(z + r\cos\phi)\sin\phi\\
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi y^2z\sin\phi + 2yrz\sin^2\phi\sin\theta + r^2z\sin^3\phi\sin^2\theta d\phi d\theta\\
  & + \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi y^2r\sin\phi\cos\phi + 2yr^2\sin^2\phi\cos\phi\sin\theta + r^3\sin^3\phi\cos\phi\sin^2\theta d\phi d\theta\\
  & = \frac{1}{4\pi}\int_0^{2\pi} 2y^2z + \pi yrz\sin\theta + \frac{4}{3}r^2z\sin^2\theta d\theta\\
  & = \frac{1}{4\pi}( 4\pi y^2z + 0 + \frac{4\pi}{3}r^2z) = y^2z + \frac{1}{3}r^2z.
\end{align}$$

Thus

$$\overline f(x,y,z,r) = x^3 + y^2z + (x + z/3)r^2,$$

and

$$\overline f_r(x,y,z,r) = x^3 + y^2z + 2(x + z/3)r,$$

and by Kirchhoff's Formula

$$\begin{align}
u(x,y,z,t)
  & = \overline f(x,y,z,ct) + ct\overline f_r(x,y,z,ct) = (x^3 + y^2z + 2(x + z/3)ct\\
  & = x^3 + y^2z + (x + z/3)c^2t^2 + ct(2(x + z/3)ct)\\
  & = x^3 + y^2z + (3x + z)c^2t^2
\end{overline}

One can now double-check $$u_{tt} = 2c^2(3x+z)$$ and $$\Delta u = 6x + 2z$$, so that $$u_{tt} = c^2u_{xx}$$.




