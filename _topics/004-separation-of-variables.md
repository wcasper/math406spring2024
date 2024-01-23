---
layout: page
title: Separation of Variables
---

Our most important tool for solving PDEs like the heat equation, the wave equation, and Poisson's equation is **separation of variables**.
The idea of separation of variables is to search for solutions of a *very special form*, where the solution is a product of single variable functions.

For example, for the heat equation

$$T_t = kT_{xx}$$

we look for solutions of the form

$$T(x,t) = F(x)G(t).$$

Inserting this into the differential equation, we get

$$G'(t)F(x) = kG(t)F''(x).$$

Now we separate the eqution to gather all the variables of one type on different sides:

$$G'(t)/G(t) = kF''(x)/F(x).$$

On the left, we have a function of $$t$$ only and on the right we have a function of $$x$$ only, so *both* sides must be constant.
Since they are equal, the must be the *same* constant which we call $$-\lambda$$:

$$G'(t)/G(t) = -\lambda,$$
$$kF''(x)/F(x) = -\lambda.$$

These are both ODEs, which we solve in the usual way, obtaining

$$G(t) = Ce^{-\lambda t}.$$

$$F(x) = A\cos\left(\sqrt{\frac{\lambda}{k}}t\right) + B\sin\left(\sqrt{\frac{\lambda}{k}}t\right),$$

where here $$A$$, $$B$$, and $$C$$ are arbitrary constants.  
Putting this all together, we get the solution 

$$T(x,t) = AC\cos\left(\sqrt{\frac{\lambda}{k}}\right)te^{-\lambda t} + BC\sin\left(\sqrt{\frac{\lambda}{k}}t\right)e^{-\lambda t}.$$

Note by the arbitrariness of $$A$$ and $$B$$, the constant $$C$$ is redundant and can be taken to be $$1$$.
This leaves us with the final expression

$$T(x,t) = A\cos\left(\sqrt{\frac{\lambda}{k}}\right)te^{-\lambda t} + B\sin\left(\sqrt{\frac{\lambda}{k}}t\right)e^{-\lambda t}.$$


which is a solution of the heat equation for all $$A,B$$ and $$\lambda \geq 0$$.
This kind of solution is called a **separable solution**.

:warning: Here we assumed that $$\lambda/k > 0$$, which turns out to be a natural assumption for solving the types of boundary value problems that we mentioned previously.  If instead $$\lambda = 0$$ we get $$F(x) = A + Bx$$ and if $$\lambda/k < 0$$, we get $$F(x) = Ae^{\sqrt{-\lambda/k}t} + Be^{-\sqrt{-\lambda/k}t}.$$

## Solving boundary value problems

In practice, there's actully a lot more restriction tht we need to imposee on the values of $$A$$, $$B$$, and $$\lambda$$ above.
These restrictions come from the boundary conditions!

### Homogeneous Dirichlet
If we have the homogeneous Dirichlet boundary conditions

$$T(0,t) = 0\quad\text{and}\quad T(L,t) = 0.$$

Using the form of $$T(x,t)$$ above, this imposes the conditions

$$A = 0\quad\text{and}\quad B\sin\left(\sqrt{\frac{\lambda}{k}}L\right)e^{-\lambda L} = 0.$$

If $$B = 0$$, then $$T$$ itself is identically zero, which is a pretty uninteresting solution.
To get nontrivial solutions, we must have $$\sin\left(\sqrt{\frac{\lambda}{k}}L\right) = 0$$, which imposes the constraint
$$\sqrt{\frac{\lambda}{k}}L = n\pi$$ for some integer $$n\in\matahbb{Z}$$.
Thus

$$\lambda = \frac{n^2\pi^2k}{L^2},\quad n\in\mathbb{Z}.$$

Thus we see that the only nontrivial separable solutions are constant multiples of

$$T_n(x,t) = \sin\left(\frac{n\pi}{L}x\right)e^{-\frac{n^2\pi^2k}{L^2}t},\quad n = 1,2,3,\dots$$

### Homogeneous Neumann
If we have the homogeneous Dirichlet boundary conditions

$$T_x(0,t) = 0\quad\text{and}\quad T_x(L,t) = 0.$$

Using the form of $$T(x,t)$$ above, this imposes the conditions

$$-A\sqrt{\frac{\lambda}{k}}\sin\left(\sqrt{\frac{\lambda}{k}}L\right)e^{-\lambda L} = 0\quad\text{and}\quad B = 0.$$

If $$A = 0$$, then $$T$$ itself is identically zero, giving us the trivial solution.
To get nontrivial solutions, we must have $$\sin\left(\sqrt{\frac{\lambda}{k}}L\right) = 0$$, which imposes the same constraint as before!

$$\lambda = \frac{n^2\pi^2k}{L^2},\quad n\in\mathbb{Z}.$$

Thus we see that the only nontrivial separable solutions are constant multiples of

$$T_n(x,t) = \cos\left(\frac{n\pi}{L}x\right)e^{-\frac{n^2\pi^2k}{L^2}t},\quad n = 0,1,2,3,\dots$$

:warning: Note that in the Neumann case, there is a value for $$n=0$$.

These aren't all the solutions of the heat equation with Dirichlet or Neumann boundary conditions.  To find more, we rely on an important property of linear PDE's, called the **superposition principle**.


