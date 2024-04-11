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

$$v_{tt} = c^2v_{\rho\rho},$$

so that $$v(\rho,t)$$ is a solution of the wave equation in one dimension!  Using d'Alembert's formula, we find

$$v(\rho,t) = \frac{1}{2}(f(\rho+ct) + f(\rho-ct)) + \frac{1}{2c}\int_{\rho-ct}^{\rho+ct} g(s)ds.$$

Thus a spherically symmetric wave will look like

$$u(\rho,t) = \frac{1}{2\rho}(f(\rho+ct) + f(\rho-ct)) + \frac{1}{2\rho c}\int_{\rho-ct}^{\rho+ct} g(s)ds.$$


## Method of spherical means

So far, we've managed to solve the wave equation in three dimension, provided that the initial condition is spherically symmetric around the origin.
In fact, since translating a solution of the wave equation gives us another solution of the wave equation, we can actually solve the wave equation for initial conditions that are spherically symmetric around a point other than the origin.

To solve the wave equation with a more general initial condition is more difficult.

We rely instead on the idea of *spherical means*.

**Definition:**  The **spherical mean** of radius $$r$$ of a function $$f(x,y,z)$$ at the point $$(x,y,z)$$ is the average value of the function $$f$$ over the surface of a sphere of radius $$r$$ centered at $$(x,y,z)$$

$$f(x,y,z;r) = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\sin\phi d\phi d\theta.$$

Importantly, notice that when $$f$$ is continuous

$$\begin{align}
\lim_{r\rightarrow 0+} f(x,y,z;r)
  & = \lim_{r\rightarrow 0+}\frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\sin\phi d\phi d\theta\\
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi \lim_{r\rightarrow 0+}f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\sin\phi d\phi d\theta\\
  & = \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi f(x,y,z)\sin\phi d\phi d\theta = f(x,y,z).
\end{align}$$

Therefore the value of a function $$f(x,y,z)$$ can be recovered from its spherical means.

We first establish an important lemma about spherical means.

**Lemma:**

$$\frac{\partial}{\partial r} f(x,y,z;r) = \frac{1}{4\pi r^2}\int_{B_r(x,y,z)} f dV.$$

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
\frac{\partial}{\partial r} f(x,y,z;r)
  & \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi \frac{\partial}{\partial r}f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\sin\phi d\phi d\theta\\
  & \frac{1}{4\pi}\int_0^{2\pi}\int_0^\pi  \nabla f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\cdot\hat n(\theta,\phi)\sin\phi d\phi d\theta\\
  & \frac{1}{4\pi r^2}\int_0^{2\pi}\int_0^\pi \nabla f(x + r\sin\phi\cos\theta,y + r\sin\phi\sin\theta,z + r\cos\phi)\cdot\hat n(\theta,\phi) r^2\sin\phi d\phi d\theta\\
  & \frac{1}{4\pi r^2}\iint_{\partial B_r(x,y,z)}  \nabla f\cdot \hat n dS\\
  & \frac{1}{4\pi r^2}\iiint_{B_r(x,y,z)} \Delta f dS
\end{align}$$

:black_square_button:

This lemma is particularly useful in the case that $$u(\vec x, t)$$ is a solution of the wave equation
$$u_{tt} = c^2\Delta u$$.  

In this case, the 




