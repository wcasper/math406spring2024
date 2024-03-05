---
layout: page
title: Unbounded Poisson's equation
---

We first consider solving Poisson's equation in the unbounded domain $$\mathbb{R}^2$$

$$u_{xx} + u_{yy} = \rho(x,y),\ \ (x,y)\in\mathbb R^2.$$

In practice, this might be used to model something like the gravitational field caused by a collection of planets.
Far away from the planets, we shouldn't feel their gravitational presence at all, so we often impose the condition that

$$u(x,y)\rightarrow 0,\ \ \text{as}\ \ \sqrt{x^2+y^2}\rightarrow\infty.$$

Our key tool for this is again the Fourier transform.  However, this time we will be using a **multidimensional Fourier transform**

$$\hat u(\xi_x,\xi_y) = \int_{\mathbb R}\int_{\mathbb R} u(x,y)e^{-2\pi i(x\xi_x+y\xi_y)}dydx.$$

This is simply what we get after taking the Fourier transform with respect to $$x$$ and then with respect to $$y$$.


## Green's function
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

Mathematically, to find $$\Phi(x,y)$$, we rely on the two-dimnsional Fourier transform.
Taking the Fourier transform of both sides of the above equation, we get

$$-4\pi^2(\xi_x^2 + \xi_y^2)\hat \Phi = 1.$$

Therefore the function we are looking for satisfies

$$\hat\Phi(\xi_x,\xi_y) = \frac{-1}{4\pi^2(\xi_x^2+\xi_y^2)}.$$

Consequently

$$\begin{align}
\Phi(x,y)
  & = \int_{\mathbb R}\int{\mathbb R} \frac{-1}{4\pi^2(\xi_x^2+\xi_y^2)} e^{2\pi i(x\xi_x + y\xi_y)} d\xi_x d\xi_y\\
  & = -\int_{\mathbb R}\int{\mathbb R} \int_0^\infty e^{2\pi i(x\xi_x + y\xi_y)-4\pi^2 t(\xi_x^2+\xi_y^2} dt d\xi_x d\xi_y\\
  & = -\int_0^\infty\left(\int_{\mathbb R}e^{2\pi ix\xi_x -4\pi^2\xi_x^2t}d\xi_x\right)\left(\int_{\mathbb R}  e^{2\pi iy\xi_y -4\pi^2\xi_y^2t}d\xi_y\right)dt\\
  & = -\frac{1}{4\pi}\int_0^\infty\frac{1}{t}e^{-(x^2+y^2)/4t}dt\\
  & = -\frac{1}{4\pi}\int_0^\infty u^2e^{-(x^2+y^2)u^2/4}dt\\
\end{align}$$


