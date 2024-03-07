---
layout: page
title: Unbounded Poisson's equation
---

We first consider solving Poisson's equation in the unbounded domain $$\mathbb{R}^2$$

$$u_{xx} + u_{yy} = \rho(x,y),\ \ (x,y)\in\mathbb R^2.$$

In practice, this might be used to model something like the gravitational field caused by a collection of planets.
Far away from the planets, we shouldn't feel their gravitational presence at all, so we often impose the condition that

$$u(x,y)\rightarrow 0,\ \ \text{as}\ \ \sqrt{x^2+y^2}\rightarrow\infty.$$


## Fundamental solution in two dimensions
To solve the Poisson's equation in the unbounded domain $$\mathbb R^2$$, we start by searching for a special function $$\Phi$$ called the **fundamental solution of Laplace's equation** in $$\mathbb{R}^2$$, which satisfies

$$\Phi_{xx} + \Phi_{yy} = \delta(x)\delta(y).$$

Physically, such a function can be interpreted as the gravitational field induced by a point mass centered at the origin.
If one is familiar with the inverse square law for gravitational and electric force fields, one might even have a guess at what $$\Phi$$ might look like.
If we can find such a function, then for any other function $$\rho(x,y)$$, then the two-dimensional convolution

$$(\Phi * \rho)(x,y) = \int_{\mathbb R}\int_{\mathbb R} \Phi(x-s,y-t)\rho(s,t)dtds$$

will automatically satisfy

$$\Delta (\Phi * \rho) = \int_{\mathbb R}\int_{\mathbb R} \Delta \Phi(x-s,y-t)\rho(s,t)dtds = \int_{\mathbb R}\int_{\mathbb R} \delta(x-s)\delta(y-t)\rho(s,t)dtds = \rho(x,y).$$

In other words, the convolution will solve

$$u_{xx} + u_{yy} = \rho(x,y),\ \ (x,y)\in\mathbb R^2.$$

Mathematically, to find $$\Phi(x,y)$$, we convert to polar coordinates 

$$r^2u_{rr} + ru_r + u_{\theta\theta} = r^2\delta(r) = 0.$$

Then we try to find a radially symmetric solution $$u(r,\theta) = u(r)$$, leading to the differential equation

$$r^2u''(r) + ru'(r) = 0.$$

The general solution of this equation is $$u(r) = A + B\ln(r)$$.

Now if $$\Delta u = \delta(r)$$, then integrating over a circle of radius $$R$$ centered at the origin, we get

$$\begin{align}
1 &= \iint_{D_R(0,0)} \delta(r) dA = \iint_{D_R(0,0)} \Delta u dA\\
  &= \oint_{\partial D_R(0,0)} \nabla u \cdot d\hat r = \oint_{\partial D_R(0,0)} u_r \cdot ds = 2\pi B.
\end{align}$$

Therefore $$B = 1/2\pi$$.  The value of $$A$$ can be anything and by choosing a different value, we only change the resulting solutions of Poisson's equation by a constant.
By convention, we take $$A = 0$$.

Thus we have

**Theorem:** The fundamental solution of Laplace's equation on $$\mathbb{R}^2$$ is

$$\Phi(x,y) = \frac{1}{2\pi}\ln{\sqrt{x^2+y^2}}.$$

## Fundamental solution in $$n$$ dimensions

One strategy to get the fundamental solution in $$n$$ dimensions is to convert the Laplacian into $$n$$-dimensional spherical coordinates.
However, we have an alternative beautiful strategy.
Our key tool for this is the **$$n$$-dimensional Fourier transform**

$$\hat u(\mathbf\xi) = \int_{\mathbb R^n} u(\mathbf x)e^{-2\pi i \mathbf x\cdot\mathbf\xi}d \mathbf x.$$


Here $$\mathbf x = (x_1,\dots,x_n)$$ and $$\mathbf \xi = (\xi_1,\dots,\xi_n)$$.
This is simply what we get after taking the Fourier transform with respect to each of the variables one at a time.

Using this, we compute the Fourier transform of Poisson's equation

$$\Delta \Phi = \delta(\mathbf x)$$

to be

$$-4\pi^2\lvert \mathbf \xi\rvert^2 \hat \Phi = 1$$

so that

$$\hat \Phi = \frac{-1}{4\pi^2\lvert \mathbf \xi\rvert^2}.$$

$$\begin{align}
\Phi(\mathbf x)
  & = \int_{\mathbb R^n} \frac{-1}{4\pi^2 \lvert \mathbf\xi\rvert} e^{2\pi i \mathbf x\cdot\mathbf \xi} d\mathbf\xi\\
  & = -\int_{\mathbb R^n} \int_0^\infty e^{2\pi i\mathbf x\cdot\mathbf \xi - 4\pi^2 t\mathbf \lvert\xi\rvert^2} dt d\mathbf \xi\\
  & = -\int_0^\infty\prod_{j=1}^n\left(\int_{\mathbb R}e^{2\pi ix_j\xi_j -4\pi^2\xi_j^2t}d\xi_x\right)
  & = -\frac{1}{(4\pi)^{n/2}}\int_0^\infty \frac{1}{t^{n/2}}e^{-\lvert \mathbf x\rvert^2/4t}dt\\
  & = -\frac{2}{(4\pi)^{n/2}}\int_0^\infty u^{n-3}e^{-\lvert \mathbf x\rvert^2u^2/4}du\\
  & = -\frac{\Gamma((n+1)/2)}{2\pi^{(n+1)/2}\lvert \mathbf x\rvert^{n-2}}
\end{align}$$





