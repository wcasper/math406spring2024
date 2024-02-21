---
layout: page
title: Nonhomogeneous Heat Equation
---

Motivated by the exploration of the last section, we wish to study solutions of the **nonhomogeneous heat equation**

$$T_t = kT_{xx} + \phi(x,t).$$

As we saw before, $$\phi(x,t)$$ shows up when we change from a nonhomogeneous boundary condition to a homogeneous one.
However, it's actually much more natural than that.
Physically, the function $$\phi(x,t)$$ can be thought of as an external heat source or sink that is input into our system, which happen for example if we held a match to some point of our rod.
Thinking about things that way, we should really have been thinking about this more general version of the heat equation the whole time!

## Solving with homogeneous boundary conditions

As we saw previously, we can change a nonhomogeneous boundary into a homogeneous one, so it is sufficient to learn how to solve homogeneous BVPs for the nonhomogeneous heat equation.
Just as in the homogeneous setting, our strategy will differ depending on whether the boundary condition is Dirichlet or Neumann.

We will solve this in detail for the Dirichlet BVP, leaving the Neumann case as a good exercise for the reader to try.
We wish to solve the BVP

$$u_t = ku_{xx} + \phi(x,t),\ \ u(0,t) = 0,\ \ u(L,t) = 0,\ \ u(x,0) = f(x).$$

To do so, think of $$t$$ temporarily as a constant and take the **sine series** of $$u(x,t)$$:

$$u(x,t) = \sum_{n=1}^\infty B_n(t)\sin\left(\frac{n\pi x}{L}\right).$$

Here the coefficients of the sine expansion depend on $$t$$, since they will differ based on the value of the time.
Likewise, we take the sine series expansion of $$\phi(x,t)$$

$$\phi(x,t) = \sum_{n=1}^\infty \phi_n(t)\sin\left(\frac{n\pi x}{L}\right).$$

Now assuming that these series are locally uniformly convergent, we can take derivatives inside the sums.
This leads to the equation

$$\sum_{n=1}^\infty B_n'(t)\sin\left(\frac{n\pi x}{L}\right) = k\sum_{n=1}^\infty -\left(\frac{n\pi }{L}\right)^2B_n(t)\sin\left(\frac{n\pi x}{L}\right) + \sum_{n=1}^\infty \phi_n(t)\sin\left(\frac{n\pi x}{L}\right).$$

We can compress this into the single sum

$$\sum_{n=1}^\infty \left(B_n'(t) + \frac{kn^2\pi^2}{L^2}B_n(t) - \phi_n(t)\right)\sin\left(\frac{n\pi x}{L}\right) = 0.$$

Now since the sine expansion of $$0$$ is unique, this implies that for all $$n$$, $$B_n(t)$$ is solution of the first-order linear ODE

$$B_n'(t) + \frac{kn^2\pi^2}{L^2}B_n(t) - \phi_n(t) = 0.$$

You can solve this equation using whatever your favorite method of solution is: integrating factors, variation of parameters, or the Laplace transform.
Any way you do it, the answer comes out to be

$$B_n(t) = e^{-\frac{n^2\pi^2}{L^2}kt}\int \phi_n(t)e^{-\frac{n^2\pi^2}{L^2}kt}dt.$$

With this formula in mind

$$u(x,t) = \sum_{n=1}^\infty B_n(t)\sin\left(\frac{n\pi x}{L}\right)$$

is a solution of the differential equation.

Now there's an interesting thing happening here: each of these integrals has its own arbitrary constant of integration.  So it seems like we've actually found infinitely many solutions of our BVP, rather than just one.
This of course isn't true, since we forgot something!  We left out our initial condition.

To fix this, we check out what the initial condition says in terms of the structure of the solution we found.
It says

$$f(x) = u(x,0) = \sum_{n=1}^\infty B_n(0)\sin\left(\frac{n\pi x}{L}\right).$$

This says that the initial values $$B_n(0)$$ of the $$B_n(t)'s$$ should come from the sine series expansion of $$f(x)$$.
In other words, if $$f(x) = \sum_{n=1}^\infty b_n\sin\left(\frac{n\pi x}{L}\right)$$, then the values of $$B_n(t)$$ are given *without an arbitrary constant* by the definite integrals

$$B_n(t) = e^{-\frac{n^2\pi^2}{L^2}kt}\left(\int_0^t \phi_n(s)e^{-\frac{n^2\pi^2}{L^2}ks}ds + b_n\right).$$

## Summary of method

It's worth summarizing the results of our derivation above in both the Dirichlet and Neumann cases.
In each case, these are the steps we use to solve each BVP.

### Dirichlet case

To solve the BVP

$$u_t = ku_{xx} + \phi(x,t),\ \ u(0,t) = 0,\ \ u(L,t) = 0,\ \ u(x,0) = f(x)$$

we do the following.

1. Calculate the coefficients of the sine expansion of $$f(x)$$:

$$f(x) = \sum_{n=1}^\infty b_n\sin\left(\frac{n\pi x}{L}\right).$$

2. Calculate the coefficients of the sine expansion of $$\phi(x,t)$$ in $$x$$ for every time $$t$$:

$$\phi(x,t) = \sum_{n=1}^\infty \phi_n(t)\sin\left(\frac{n\pi x}{L}\right).$$

3. Calculate $$B_n(t)$$ for each $$n$$ using the following formula

$$B_n(t) = e^{-\frac{n^2\pi^2}{L^2}kt}\left(\int_0^t \phi_n(s)e^{-\frac{n^2\pi^2}{L^2}ks}ds + b_n\right)$$

Then the solution of the BVP is

$$u(x,t) = \sum_{n=1}^\infty B_n(t)\sin\left(\frac{n\pi x}{L}\right).$$


### Neumann

To solve the BVP

$$u_t = ku_{xx} + \phi(x,t),\ \ u_x(0,t) = 0,\ \ u_x(L,t) = 0,\ \ u(x,0) = f(x)$$

we do the following.

1. Calculate the coefficients of the cosine expansion of $$f(x)$$:

$$f(x) = \sum_{n=0}^\infty a_n\cos\left(\frac{n\pi x}{L}\right).$$

2. Calculate the coefficients of the cosine expansion of $$\phi(x,t)$$ in $$x$$ for every time $$t$$:

$$\phi(x,t) = \sum_{n=0}^\infty \phi_n(t)\cos\left(\frac{n\pi x}{L}\right).$$

3. Calculate $$A_n(t)$$ for each $$n$$ using the following formula

$$A_n(t) = e^{-\frac{n^2\pi^2}{L^2}kt}\left(\int_0^t e^{-\frac{n^2\pi^2}{L^2}ks}ds + a_n\right)$$

Then the solution of the BVP is

$$u(x,t) = \sum_{n=0}^\infty A_n(t)\cos\left(\frac{n\pi x}{L}\right).$$





