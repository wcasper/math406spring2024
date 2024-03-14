---
layout: page
title: Uniqueness of Solutions to Poissons Equation
---

Just like the case of the heat equation, we are interested in whether or not it
is possible for a given boundary value problem for Poisson's equation to have a
unique solution.

We again use the energy method strategy, though in this case the energy of a solution of Poisson's equation

$$\Delta u= \rho(\vec x),\ \ \vec x\in\Omega,\ \ \ u(\vec x) = g(\vec x),\ \ \vec x\in\partial\Omega$$

is defined by 
$$E(u)  = \int_{\Omega} \lvert \nabla u\rvert^2 dV.$$

Clearly this quantity is non-negative.
Furthermore, the Divergence Theorem allows us to write

$$\begin{align}
E(u)
& = \int_{\Omega} \lvert \nabla u\rvert^2 dV\\
& = \int_{\Omega} \nabla\cdot (u\nabla u)dV - \int_{\Omega} u\Delta u dV\\
& = \int_{\Omega} \nabla\cdot (u\nabla u)dV - \int_{\Omega} u\rho dV\\
& = \int_{\partial\Omega} g\nabla u \cdot \hat n dS - \int_{\Omega} u\rho dV
\end{align}$$


Now suppose that $$u(\vec x)$$ and $$v(\vec x)$$ are both solutions of Poisson's equation with the nonhomogeneous boundary condition above.
Then $$w = u-v$$ is a solution of 

$$\Delta w= 0,\ \ \vec x\in\Omega,\ \ \ w(\vec x) = 0,\ \ \vec x\in\partial\Omega.$$

In this case, the energy of $$w$$ is given by

$$\begin{align}
E(w)
& = \int_{\partial\Omega} 0\nabla w \cdot \hat n dS - \int_{\Omega} w0 dV = 0\\
\end{align}$$

Therefore

$$\int_{\Omega} \lvert \nabla w\rvert^2 dV = 0$$, and since the integrand is continuous and nonnegative, we must have $$\nabla w = \vec 0$$ for all $$\vec x\in\Omega$$.
Hence $$w$$ is constant in $$\Omega$$ and by the boundary condition that $$w$$ is zero on the boundary, $$w$$ must be identically zero.
Hence $$u=v$$.

To summarize, we have the following theorem.

**Theorem:** If $$u$$ and $$v$$ are two solutions of Poisson's equation with the nonhomogeneous boundary condition

$$\Delta u= \rho(\vec x),\ \ \vec x\in\Omega,\ \ \ u(\vec x) = g(\vec x),\ \ \vec x\in\partial\Omega$$

which extend to continuous functions in a neighborhood of the closure of $$\Omega$$, then $$u=v$$.



