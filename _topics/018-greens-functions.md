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

$$y'' -y = f(x),\ \ y(\pi/2) = 0,\ y(\pi = 0).$$

To solve this, we look for the Green's function $$G(x;t)$$ which satisfies

$$G''(x;t) - G(x;t) = \delta(x-t).$$

Taking the Fourier transform, we obtain

$$-4\pi^2 \xi^2 \hatG(\xi;t) -  \hat G(\xi;t) = e^{-2\pi i \xi t}.$$

This says

$$\hatG(\xi;t) = \frac{-1}{1 + 4\pi^2\xi^2}e^{-2\pi i \xi t}$$

and therefore

$$G(x;t) = -\frac{1}{2}e^{-\lvert (x+t)\rvert}.$$

To achieve the boundary condition, we can add on any solution of the homogeneous equation $$y''-y=0$$.
To get $$G(\pm \pi;t) = 0$$, we thus obtain

$$G(x;t) = -\frac{1}{2}e^{-\lvert (x+t)\rvert} - \frac{1}{2}e^{-\lvert (\pi+t)\rvert}\cos(x)+\frac{1}{2}e^{-\lvert (\pi/2+t)\rvert}\sin(x).$$

**Example:**  Consider Poisson's equation on the disk $$\Omega = D_R(0,0)$$

$$u_{xx} + u_{yy} = \rho(x,y),\ \ (x,y)\in D_R(0,0).$$

The Green's function for this equation satisfies

$$G_{xx}(x,y;s,t) + G_{yy}(x,y;s,t) = \delta(x-s,y-t),\ \ (x,y)\in D_R(0,0).$$

As we saw previously, the solution of this equation is

$$G(x,y;s,t) = \frac{1}{2\pi}\ln \sqrt{(x-s)^2+(y-t)^2} + B$$

for any constants $$A$$ and $$B$$.
To satisfy the boundary condition $$G(x,y;s,t) = 0$$ for $$(x,y)\in\partial D_R(0,0)$$, we should take $$B = -\frac{1}{2\pi}\ln(R)$$.
Thus the Green's function is

$$G(x,y;s,t) = \frac{1}{2\pi}\ln \frac{\sqrt{(x-s)^2+(y-t)^2}}{R}.$$

**Example:**  The Green's function for Poissn's equation on the upper half plane $$\mathbb H = \{(x,y): y>0\}$$ is given by

$$G(x,y;s,t) = \frac{1}{4\pi}\ln \frac{(x-s)^2+(y-t)^2}{(x-s)^2+(y+t)^2}.$$


## Solving boundary value problems for Poisson's equation

Suppose that we want to solve Poisson's equation on a domain $$\Omega$$ with a Dirichlet boundary condition

$$u_{xx} + u_{yy} = \rho(x,y), \ \ (x,y)\in\Omega,\ \ \text{with}\ \ u(x,y) = g(x,y),\ \ (x,y)\in\partial\Omega.$$

We first change this to a homogeneous boundary condition by setting $$u = v + g$$.
This leads to the differential equation

$$\Delta v = \rho-\Delta g,\ \ (x,y)\in\Omega,\ \ \text{with}\ \ v(x,y) = 0,\ \ (x,y)\in\partil\Omega.$$

We can then solve this with the Green's function for $$\Delta$$ on $$\Omega$$:

$$v(x,y) = \iint_{\Omega} G(x,y;s,t)(\rho(s,t)-\Delta g(s,t))dsdt.$$

Now by Green's Theorem

$$\iint_{\Omega} f\Delta g-g\Delta f dA = \oint_{\partial\Omega} (f\nabla g - g\nabla f)\cdot\hat n dC.$$

Using this, we get

$$\begin{align}
u(x,y)
  & = g(x,y) + \iint_{\Omega} G(x,y;s,t)(\rho(s,t)-\Delta_{s,t} g(s,t))dsdt\\
  & = \iint_{\Omega} G(x,y;s,t)\rho(s,t)dsdt - \oint_{\partial\Omega} G(x,y;s,t)\nabla_{s,t} g(s,t)\cdot\hat n - g(s,t)\nabla_{s,t} G(x,y;s,t)\cdot\hat n dC(s,t) \\
  & = \iint_{\Omega} G(x,y;s,t)\rho(s,t)dsdt + \oint_{\partial\Omega} g(s,t)\nabla_{s,t} G(x,y;s,t)\cdot\hat n dC(s,t).
\end{align}$$

where here $$\hat n$$ is the normal unit vector pointing outward from the interior of the curve $$\partial \Omega$$.

The function $$P(x,y;s,t) = \nabla_{s,t} G(x,y;s,t)\cdot \hat n$$ defined on the boundary of $$\Omega$$ is called the **Poisson kernel** of $$\Omega$$.

**Example:**
Recall the Green's function for $$D_R(0,0)$$ is

$$G(x,y;s,t) = \frac{1}{2\pi}\ln \frac{\sqrt{(x-s)^2+(y-t)^2}}{R}.$$

The gradient is

$$\nabla_{s,t} G(x,y;s,t) = \frac{1}{2\pi}\frac{1}{\sqrt{(x-s)^2+(y-t)^2}} \lvert s-x,t-y\rvert$$ 

and unit vector $$\hat n$$ at a point $$(s,t)\in\partial D_R(0,0)$$ is $$\hat n = \frac{1}{\sqrt{s^2+t^2}}\lvert s,t\rvert = \frac{1}{R}\lvert s,t\rvert$$, so the Poisson kernel is

$$P(x,y;s,t) = \frac{1}{2\pi}\frac{s^2-sx + t^2-ty}{\sqrt{(x-s)^2+(y-t)^2}}.$$

If we parameterize the boundary as $$s = R\cos(\phi)$$ and $$t = R\sin(\phi)$$, and switch to polar coordinates $$x = r\cos\theta$$ and $$y=r\sin\theta$$, this becomes

$$P(r,\theta;\phi) = \frac{1}{2\pi}\frac{R^2-Rr\cos(\theta-\phi)}{R^2 + r^2 - 2rR\cos(\theta-\phi)}.$$


