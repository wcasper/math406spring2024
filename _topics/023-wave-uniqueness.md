---
layout: page
title: Uniqueness of Solutions to the Wave Equation
---


The **kinetic energy** of the wave equation in a domain $$\Omega\subseteq\mathbb{R}^n$$ at time $$t$$ is

$$\text{KE}(t) = \int_{\Omega} \frac{1}{2}u_t^2 d\vec x.$$

The **potential energy** of the wave equation in a domain $$\Omega\subseteq\mathbb{R}^n$$ at time $$t$$ is

$$\text{PE}(t) = \int_{\Omega} \frac{1}{2}c^2\lvert\nabla u\rvert^2 d\vec x.$$

The **total energy** $$\text{E}(t)$$ is the sum of the kinetic and potential energy.

With Dirichlet boundary conditions, the total energy is conserved, meaning that it is constant in time.

To see this, start by supposing that

$$u_{tt} = c^2\Delta u,\ \ \text{with}\ \ u = 0,\ \text{on}\ \partial\Omega.$$

The **product rule with gradients** implies that

$$\nabla\cdot (f\nabla g) = (\nabla f)\cdot(\nabla g) + f\Delta g.$$

In particular this implies

$$u_t\Delta u = \nabla\cdot (u_t\nabla u) - (\nabla u_t\cdot\nabla u).$$

Using this combined with the divergence theorem

$$\begin{align}
\text{KE}'(t)
  & = \frac{\partial}{\partial t}\int_{\Omega} \frac{1}{2}u_t^2 d\vec x\\
  & = \int_{\Omega} u_tu_{tt} d\vec x\\
  & = \int_{\Omega} c^2u_t\Delta u d\vec x\\
  & = \int_{\Omega} c^2\nabla\cdot (u_t\nabla u)d\vec x - \int_{\Omega}c^2(\nabla u_t\cdot\nabla u) d\vec x\\
  & = \int_{\partial\Omega} c^2u_t\nabla u \cdot \hat n d S - \int_{\Omega}c^2(\nabla u_t\cdot\nabla u) d\vec x\\
  & = - \int_{\Omega}c^2(\nabla u_t\cdot\nabla u) d\vec x\\
  & = - \frac{\partial}{\partial_t}\int_{\Omega}c^2\frac{1}{2}(\nabla u\cdot\nabla u) d\vec x\\
  & = - \text{PE}'(t).
\end{align}$$

Combining this together, we find

$$\text{E}'(t) = \text{KE}'(t) + \text{PE}'(t) = 0.$$

This means that $$E(t)$$ must be constant.

## Application to uniqueness

We can use the fact that energy is conserved to prove that solutions of the wave equation, or even the *forced* wave equation, are unique as long as their total energy is finite.

**Uniqueness Theorem:** Suppose that $$u(\vec x,t)$$ is a solution of the forced wave equation 

$$u_{tt} = c^2\Delta u + \phi(\vec x, t),\ \ u = 0\ \text{on}\ \partial\Omega$$

with the initial condition $$u(x,0) = f(x)$$ and $$u_t(x,0) = g(x)$$.
If $$v$$ is a second solution of the equation with the same initial condition and boundary condition, then $$u=v$$.

**Proof:**

Consider the function $$w = u-v$$.
It is easy to check that $$w$$ is a solution of the usual wave equation with Dirichlet boundary conditions

$$w_{tt} = c^2\Delta w,\ \ w = 0\ \text{on}\ \partial\Omega$$

and also satisfies the initial condition $$w(x,0) = 0$$ and $$w_t(x,0) = 0$$.

Then the initial kinetic and potential energy of $$w$$ is zero, so the initial total energy of $$w$$ is zero.
Since energy is conserved, $$w$$ has zero energy at every time $$t$$.
This implies that the kinetic and potential energy of $$w$$ is zero at every time.
The kinetic energy is the integral of the non-negative continuous function $$w_t^2$$, so this implies that $$w_t^2=0$$ in $$\Omega$$.
Likewise, the potential energy being zero implies $$\nabla w = \vec 0$$.
In other words, all the derivatives of $$w$$ are zero and this implies that $$w$$ is a constant.
Since $$w$$ must be zero on the boundary, this constant must be zero.
Hence $$w=0$$ in $$\Omega$$ and this implies $$u=v$$.
:black_square_button:


