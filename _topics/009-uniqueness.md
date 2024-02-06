---
layout: page
title: Uniqueness of Solutions
---

The technology we just developed shows us how to find a solution of the heat equation

$$T_t = kT_{xx}.$$

However, a very important question remains: is the solution unique?

In this section, we will show that the solutions of Dirichlet, Neumann, or mixed boundary value problems are indeed unique.
The technique we apply comes from understanding the *physics* of the situation.
The temperature of a material is a measurement of the average speed of the individual molecules.
For this reason

$$E(t) = \int_0^L \frac{1}{2}T^2(x,t)dx$$

is a mathematical expression for the total energy of the system as a function of time.
Under homogeneous boundary conditions, no new energy is being introduced to the system, so the only possibility is that the energy either stays the same or leaves the system.
In other words, the physics suggests that $$E'(t)\leq 0$$ for all $$t$$.
This is what we prove.
Then by using this, we show tht solutions to boundary value problems (not necessarily homogeneous) are unique.
This kind of method of proving uniqueness is called an **energy method** and is used for other classical PDEs.

# Energy method

**Definition:** Let $$T(x,t)$$ be a solution of the heat equation

$$T_t = kT_{xx}$$

with either a homogeneous Dirichlet, Neumann, or mixed boundary condition.
The **energy** of this solution is

$$E(t) = \int_0^L \frac{1}{2}T^2(x,t)dx.$$

**Theorem:** Assume $$k\geq 0$$.  Then $$E'(t)\leq 0$$ for all $$t>0$$.

**Proof:**  

Using differentiation under the integral

$$\begin{align}
E'(t)
  & = \frac{d}{dt}\int_0^L T^2dx = \int_0^L \frac{\partial}{\partial t} T^2dx\\
  & = \int_0^L 2T T_tdx  = \int_0^L 2kT T_{xx} dx\\
  & = TT_x\rvert_0^L - \int_0^L 2kT_x^2dx  = 0 -2k\int_0^L T_x^2dx \leq 0.
\end{align}$$

:black_square_button:

**Theorem:** Any continuous solution of the heat equation with a Dirichlet, Neumann, or mixed boundary condition (if it exists) is unique.

**Proof:**  

Let's assume that our boundary condition is the Dirichlet condition

$$T_t = kT_xx,\quad\text{with}\quad T(0,t) = T_0(t),\ \ T(L,t) = T_1(t),\ \ T(x,0) = f(x).$$

The proof for the other types of boundary conditions will be similar.
If $$T(x,t) = u(x,t)$$ and $$T(x,t) = v(x,t)$$ are two solutions of this boundary value problem, then $$T = u-v$$ solves the *homogeneous* boundary value problem

$$T_t = kT_xx,\quad\text{with}\quad T(0,t) = 0,\ \ T(L,t) = 0,\ \ T(x,0) = 0.$$

The initial energy of this solution is

$$E(t) = \int_0^L T(x,0) dx = \int_0^L = 0,$$

and since $$E(t)\geq 0$$ and $$E'(t) \leq 0$$ for all $$t$$, it follows that $$E(t)$$ is identically zero for all $$t$$.
Hence

$$\int_0^L T(x,t)^2dx = 0$$

for all $$t\geq 0$$.  Since $$T(x,t)$$ is continuous, this implies that $$T(x,t) = 0$$ for all $$x$$ and for all $$t$$.
:black_square_button:

:warning: The assumption that the solution to the heat equation had some regularity (here continuity) was important.  This can cause complications for more complicated boundary value problems, but this is outside the purview of the current course.

