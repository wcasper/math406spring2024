---
layout: page
title: Duhamel's Principle
---

One obviously interesting situation to consider is when there is an external forcing function which is creating some source of continued perturbations over time.
This would be the case, for example, if we were modeling a drummer performing a roll on a drum head, a faucet pooring water into a half-full bath, wind driving waves over an ocean, and many other situations.
Mathematically, this is represented by the equation

$$u_{tt} = c^2\Delta u + \phi(\vec x, t),\ \ \vec x\in \Omega.$$

If we imagined for a minute that $$c = 0$$, the function $$\phi(\vec x, t)$$ is representing the second derivative of the function $$u$$ with respect to time $$t$$, so physically it represents a source of acceleration.
To solve this equation, we rely on an idea called **Duhamel's Principle**, which realizes an external forcing as equivalent to an unforced wave problem, but where the initial condition is continuously readjusted.

To understand this, imagine that we have an initial condition $$u(\vec x,0) = 0$$ and $$u_t(\vec x, 0) = 0$$ and that we want to approximate the value of $$u(\vec x,\Delta t)$$ and $$u_t(\vec x, \Delta t)$$ after a very small amount of time $$\Delta t$$.
To do this, we use the idea that for very small values of $$\Delta t$$,

$$f'(a+\Delta t) = f'(a) + f''(a)\Delta t\ \ \text{and}\ \ f(a+\Delta t) = f(a) + f'(a)\Delta t.$$

These are just the usual linear approximations of $$f'$$ and $$f$$, respectively, based at $$t=a$$.

In particular, this means that for any time $$t$$

$$u_t(\vec x,\Delta t) \approx u_t(\vec x,0) + (c^2\Delta u (\vec x, 0) + \phi(\vec x, 0))\Delta t = \phi(\vec x, 0)\Delta t$$

and also that

$$u(\vec x,\Delta t) \approx u(\vec x, 0) + u_t(\vec x, 0)\Delta t = 0.$$

This is exactly the same thing that we would get with an *unforced* wave equation, but with the initial conditions $$u(\vec x, 0) = 0$$ and $$u_t(\vec x,0) = \phi(\vec x,0)\Delta t$$.

This gives us the idea of approximating the solution of the forced wave equation

$$u_{tt} = c^2\Delta u + \phi(\vec x, t),\ \ \vec x\in \Omega,\ \ u(\vec x, 0) = 0,\ u_t(\vec x,0) = 0$$

with the iterated process where we find approximate solutions in the interval $$[0,\Delta t]$$, the interval $$[\Delta t,2\Delta t]$$, and so on.
This means solving the unforced  wave equation

$$u^k_{tt} = c^2\Delta u^k$$

with the initial condition

$$u^k(\vec x, k\Delta t) = 0,\ \ u^k_t(\vec x,k\Delta t) = \phi(\vec x,k\Delta t)\Delta t, k\Delta t < t < (k+1)\Delta t.$$

The value of $$u$$ at the time $$n\Delta t$$ is then given by adding up the approximations of $$u$$ on each of the given intervals

$$u(\vec x,n\Delta t) = \sum_{k=1}^n u^k(\vec x,k\Delta_t)$$

Then by taking the limit as $$\Delta t$$ goes to $$0$$, our approximations become the actual solution, and our sum becomes an integral and our $$\Delta t$$ becomes the differential expression $$dt$$ inside the integral.
This leads to the following theorem, which is also referred to as Duhamel's Principle or Duhamel's Theorem.

**Duhamel's Theorem:**  Let $$\widetilde u(\vec x,t;a)$$ be a solution of the wave equation

$$\widetilde u_{tt} = c^2\Delta \widetilde u,\ \ \vec x\in \Omega,\ \ \widetilde u(\vec x, a) = 0,\ \widetilde u_t(\vec x,a) = \phi(\vec x,a).$$

Then the function

$$u(\vec x,t) = \int_0^t \widetilde u(\vec x, t,a)da$$

is a solution of the forced wave equation

$$u_{tt} = c^2\Delta u + \phi(\vec x, t),\ \ \vec x\in \Omega$$

with the initial condition $$u(\vec x, 0) = 0$$ and $$u_t(\vec x, 0) = 0$$.





