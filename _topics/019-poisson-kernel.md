---
layout: page
title: Poisson Kernels
---

In the case of a nonhomogenous boundary value problem for Laplace's equation on the disk $$D_R(0,0)$$, we found a special function we called the Poisson kernel on the disk, with the property convolution with the boundary condition solves the boundary value problem.
It turns out this situation is not unique: any domain has a corresponding Poisson kernel, whose value may be derived from the Green's function of the domain.

To see this, we will utilize the following modified version of the Divergence Theorem (or Green's Theorem in two dimensions).

**Modified Divergence Theorem:** Let $$\Omega\subseteq \mathbb R^n$$ be a domain.  Then for any functions $$f$$ and $$g$$ which are twice differentiable in a neighborhood containing the closure of $$\Omega$$,

$$\int_{\Omega} f\Delta g - g\Delta f dV = \int_{\partial\Omega} (f\nabla g - g\nabla f)\cdot \hat n dS.$$

Here $$\hat n$$ is the normal unit vector perpendicular to the domain.

**Proof:**

By the Divergence Theorem

$$\int_{\Omega} \nabla \cdot (f\nabla g) dV = \int_{\partial\Omega} f\nabla g \cdot \hat n dS.$$

Furthermore, by the product rule we we can write this as

$$\int_{\Omega} (\nabla f)\cdot(\nabla g) dV  + \int_{\Omega} f\Delta g dV = \int_{\partial\Omega} f\nabla g \cdot \hat n dS.$$

Likewise 

$$\int_{\Omega} (\nabla g)\cdot(\nabla f) dV  + \int_{\Omega} g\Delta f dV = \int_{\partial\Omega} g\nabla f \cdot \hat n dS.$$

Subtracting these two equatins gives the desired result.

:black_square_button:

## Solving boundary value problems for Poisson's equation

Suppose that we want to solve Poisson's equation on a domain $$\Omega$$ with a Dirichlet boundary condition

$$\Delta u(\vec x) = \rho, \ \ \vec x\in\Omega,\ \ \text{with}\ \ u(\vec x) = g(\vec x),\ \ \vec x\in\partial\Omega.$$

We first change this to a homogeneous boundary condition by setting $$u = v + g$$.
This leads to the differential equation

$$\Delta v(\vec x) = \rho(\vec x)-\Delta g(\vec x),\ \ \vec x\in\Omega,\ \ \text{with}\ \ v(\vec x) = 0,\ \ \vec x\in\partial\Omega.$$

We can then solve this with the Green's function for $$\Delta$$ on $$\Omega$$:

$$v(\vec x) = \int_{\Omega} G(\vec x;\vec t)(\rho(\vec t)-\Delta g(\vec t))d\vec t.$$

Now by the Modified Divegence Theorem above and using the fact that $$G(\vec x;\vec t)$$ is $$0$$ on $$\partial \Omega$$

$$\begin{align}
u(x,y)
  & = g(\vec x) + \int_{\Omega} G(\vec x;\vec t)(\rho(\vec t)-\Delta g(\vec t))d\vec t\\
  & = g(\vec x) + \int_{\Omega} G(\vec x;\vec t)\rho(\vec t)d\vec t - \int_{\Omega}g(\vec t)\Delta G(\vec x,\vec t) d\vec t + \int_{\partial\Omega} g(\vec t)\nabla G(\vec x;\vec t)\cdot\hat n dS\\
  & = g(\vec x) + \int_{\Omega} G(\vec x;\vec t)\rho(\vec t)d\vec t - \int_{\Omega}g(\vec t)\delta_{\vec x}(\vec t) d\vec t + \int_{\partial\Omega} g(\vec t)\nabla G(\vec x;\vec t)\cdot\hat n dS\\
  & = \int_{\Omega} G(\vec x;\vec t)\rho(\vec t)d\vec t + \int_{\partial\Omega} g(\vec t)\nabla G(\vec x;\vec t)\cdot\hat n dS
\end{align}$$

This motivates th following definition.

**Definition:** The **Poisson kernel** of $$\Omega$$ is the function

$$P(\vec x;\vec t) = \nabla G(\vec x;\vec t)\cdot \hat n$$ 

where here $$\hat n$$ is the normal unit vector pointing outward from the interior of the curve $$\partial \Omega$$ at the point $$\vec t$$ and the gradient is taken in the variable $$\vec t$$.


**Example:**

The Green's function for the upper half plane $$\mathbb H = \{(x,y)\in\mathbb R^2: y > 0\}$$ is

$$\begin{align}
G(x,y;s,t)
& = \frac{1}{2\pi}\ln\sqrt{(x-s)^2+(y-t)^2} - \frac{1}{2\pi}\ln\sqrt{(x-s)^2+(y+t)^2}\\
& = \frac{1}{2\pi} \ln\sqrt\frac{(x-s)^2+(y-t)^2}{(x-s)^2+(y+t)^2}.
\end{align}$$

The normal unit vector at a boundary point $$(s,0)$$ of $$\mathbb{H}$$ is $$\hat n = \langle 0,-1\rangle$$.
The Poisson kernel is

$$P(x,y;s,t) = \nabla G \cdot\hat n = -G_t = \frac{1}{2\pi}\frac{y-t}{(x-s)^2+(y-t)^2} + \frac{1}{2\pi}\frac{y+t}{(x-s)^2+(y+t)^2}.$$

On the boundary $$t=0$$, so the expression simplifies to

$$P(x,y;s,0) = \frac{1}{\pi}\frac{y}{(x-s)^2+y^2}.$$

Because the parameter $$s$$ only appears with the $$x$$-term, we simply call

$$P(x,y) := P(x,y;0,0) = \frac{1}{\pi}\frac{y}{x^2+y^2}$$

the **Poisson kernel of the upper half plane** or the **Poisson kernel on the real line**.

As a consequence the solution of Poisson's equation

$$\Delta u = \rho(x,y),\ \ (x,y)\in\mathbb{H},\quad u(x,0) = g(x)$$

is given by

$$\begin{align}
u(x,y)
 & = \int_{\mathbb R}\int_0^\infty G(x,y;,s,t)\rho(s,t)dtds + \int_{\mathbb R} P(x-s,y)g(s)ds\\
 & = \frac{1}{2\pi}\int_{\mathbb R}\int_0^\infty \ln\sqrt\frac{(x-s)^2+(y-t)^2}{(x-s)^2+(y+t)^2}\rho(s,t)dtds + \int_{\mathbb R} \frac{1}{\pi}\frac{y}{(x-s)^2+y^2}g(s)ds\\
\end{align}$$

**Example:**

The Green's function for the disk $$D_R(0,0) = \{(x,y)\in\mathbb R^2: x^2+y^2 < R\}$$ is

$$G(x,y;s,t) = \frac{1}{2\pi}\ln \sqrt{(x-s)^2+(y-t)^2} - \frac{1}{2\pi}\ln \sqrt{(x-s^*)^2+(y-t^*)^2}+ \frac{1}{2\pi} \ln \frac{R}{\sqrt{s^2+t^2}}.$$

where here $$(s^*,t^*) = (s,t)R^2/(s^2+t^2)$$.
In polar coordinates, this can be written using the Law of Cosines as

$$\begin{align}
G(r,\theta;\nu,\phi)
  & = \frac{1}{2\pi}\ln \sqrt{r^2+\nu^2-2r\nu\cos(\theta-\phi)} - \frac{1}{2\pi}\ln \sqrt{r^2 + R^4/\nu^2 - 2r(R^2/\nu)\cos(\theta-\phi)}\\
  & = \frac{1}{2\pi}\ln \sqrt{r^2/R^2+\nu^2/R^2-2r\nu/R^2\cos(\theta-\phi)} - \frac{1}{2\pi}\ln \sqrt{\nu^2r^2/R^4 + 1 - 2r\nu/R^2\cos(\theta-\phi)}
  & = \frac{1}{2\pi}\ln \sqrt{\frac{r^2/R^2+\nu^2/R^2-2r\nu/R^2\cos(\theta-\phi)}\sqrt{\nu^2r^2/R^4 + 1 - 2r\nu/R^2\cos(\theta-\phi)}}
\end{align}$$

where $$\nu\cos\phi = s$$ and $$\nu\sin\phi = t$$.

The normal unit vector to the boundary of the disk at the point $$(\nu,\phi)$$ is $$\hat n = \hat nu$$, so the Poisson kernel is

$$\begin{align}
P(r,\theta;\nu,\phi)
& = \nabla G \cdot \hat n = G_\nu\\
& = \frac{1}{2\pi R}\frac{\nu/R - r/R\cos(\theta-\phi)}{r^2/R^2+\nu^2/R^2-2r\nu/R^2\cos(\theta-\phi)}  - \frac{1}{2\pi R}\frac{\nu r^2/R^3 - r/R\cos(\theta-\phi)}{r^2\nu^2/R^4+1-2r\nu/R^2\cos(\theta-\phi)}.
\end{align}$$

On the boundary $$\nu = R$$ and this simplifies to

$$P(r,\theta; R,\phi)  = \frac{1}{2\pi R}\frac{1 - r^2/R^2}{1+r^2/R^2-2(r/R)\cos(\theta-\phi)}.$$

This agrees with our previous expression for the Poisson kernel on the disk $$D_R(0,0)$$, up to a factor $$R$$ which vanishes upon accounting for the switch to polar coordinates in the integral.

As a consequence the solution of Poisson's equation

$$\Delta u = \rho(r,\theta),\ \ 0 < r < R,\quad u(R,\theta) = g(\theta)$$

is given by

$$\begin{align}
u(x,y)
 & = \int_0^{2\pi}\int_0^R\int_0^\infty G(r,\theta;,\nu,\phi)\rho(\nu,\phi)\nu\d\nu d\phi + \int_0^{2\pi} P(r,\theta; R,\phi)g(\phi) R d\phi\\
 & = \frac{1}{2\pi}\int_0^{2\pi}\int_0^R\int_0^\infty \ln \sqrt{\frac{r^2/R^2+\nu^2/R^2-2r\nu/R^2\cos(\theta-\phi)}\sqrt{\nu^2r^2/R^4 + 1 - 2r\nu/R^2\cos(\theta-\phi)}}\rho(\nu,\phi) \nu d\nu d\phi + \frac{1}{2\pi}\int_0^{2\pi}\frac{1 - r^2/R^2}{1+r^2/R^2-2(r/R)\cos(\theta-\phi)}.
 \end{align}$$


