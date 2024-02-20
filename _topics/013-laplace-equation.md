---
layout: page
title: Laplace Equation
---

Laplace's equation in two dimensions is the PDE

$$u_{xx} + u_{yy} = 0$$

In three dimensions, it is given by

$$u_{xx} + u_{yy} + u_{zz} = 0.$$

Due to its auspicious role in physics, the operation of taking all the (non-mixed) second derivatives and adding them together has earned itself its own name.
It is called the **Laplacian** and is denoted by $$\Delta$$.
Thus Laplaces equation in *any* dimensions can be expressed simply as

$$\Delta u = 0.$$

## Harmonic functions

A solution $$u$$ of Laplace's equation $$\Delta u = 0$$ inside a domain $$\Omega\subseteq\mathbb{R}^n$$ is called a **harmonic function on $$\Omega$$**.
Here by a **domain**, we mean a connected open subset of $$\mathbb{R}^n$$.
Inside $$\Omega$$, harmonic functions feature two important properties: the Mean Value Property and the Maximum Principle.

The value of a function which is harmonic in $$\Omega$$ is determined by the value of the function on the booundary $$\partial\Omega$$.
Geometrically in two dimensions, a harmonic function looks like what happens when you take a wooden box and sand down the sides unevenly, so that the height of each side is described by some function.
Then if you stretch a rubber sheet oveer the top and pull it as tight as possible, the resulting surfce is a solution of Laplace's equation with Dirichlet boundary conditions


$$u_{xx} + u_{yy} = 0,\ \ u(x,0) = f_1(x),\ \ u(x,M) = f_2(x),\ \ u(0,y) = g_1(y),\ \ u(L,y) = g_2(y).$$

<p align="center"><img width=600 src="fig/013-solution-visual.png"/></p>

In three dimensions, harmonic functions describe gravitatial fields in the empty spaces *between* massive objects like planets, or electric fields in the empty spaces away frmo the source of the electric charge.

## The Mean Value Property

Suppose that $$u$$ is a harmonic function on $$\Omega\subseteq\mathbb{R}^2$$.
The Mean Value Property says that for any circle in $$\Omega$$, if we take the average over the circle, then we get the value of $$u$$ at the center of the circle.


**Theorem (Mean Value Property):**  Suppose that $$u(x,y)$$ is harmonic on a domain $$\Omega\subseteq\mathbb{R}^2$$.  Then for every value of $$r$$ for which the disk

$$D_r(a,b) = \{(x,y): (x-a)^2 + (y-b)^2\leq r^2\}$$

belongs to $$\Omega$$, we have

$$\frac{1}{2\pi}\oint_0^{2\pi} u(a + r\cos(\theta),b + r\sin(\theta)) d\theta = u(a,b).$$

**Proof:**
By Green's Theorem, the integral of $$u$$ over this disk satisfies

$$\begin{align}
\iint_{D_r(a,b)} \Delta u(x,y)dA
  & = \int_{0}^{2\pi} u_x(a + r\cos(\theta),b + r\sin(\theta)) (r\sin\theta) +u_y(a + r\cos(\theta),b + r\sin(\theta)) (r\cos\theta) d\theta\\
  & = \int_{0}^{2\pi}r\frac{\partial}{\partial r} u(a + r\cos(\theta),b + r\sin(\theta)) d\theta\\
  & = r\frac{d}{d r}\int_{0}^{2\pi} u(a + r\cos(\theta),b + r\sin(\theta)) d\theta.
\end{align}$$

Then since $$\Delta u = 0$$, this says that the value of

$$\int_{0}^{2\pi} u(a + r\cos(\theta),b + r\sin(\theta)) d\theta$$

is constant in $$r$$.  Taking the limit as $$r\rightarrow 0$$, this expression becomes $$2\pi u(a,b)$$.  Hence

$$\int_{0}^{2\pi} u(a + r\cos(\theta),b + r\sin(\theta)) d\theta = 2\pi u(a,b).$$

:black_square_button:

In three dimensions, this generalizes to the average over the surface of a ball being equal to the value at the center of the ball.
This generalizes to $$n$$ dimensions by replacing surface with hypersurface.


## The Maximum Principle

The Maximum Principle states that harmonic functions take their largest values on the boundary $$\partial \Omega$$ of a domain $$\Omega$$.

**Theorem:** If $$u(x,y)$$ is harmonic on a domain $$\Omega$$ and has a global maximum in $$\Omega$$, then $$u(x,y)$$ is constant.

**Proof:** Suppose that $$u(x,y)$$ has a global maximum $$M$$ at some point in $$\Omega$$.
Then let $$E = \{(a,b)\in\Omega: u(a,b)=M\}.$$
Since $$E = u^{-1}(M)$$, and $$u$$ is continuous, $$E$$ is closed.
Moreover, suppose $$(a,b)\in E$$.
Since $$\Omega$$ is open, there exists $$r>0$$ such that $$D_r(a,b)\subseteq\Omega$$.
By the Mean Value Property 

$$0 = \frac{1}{2\pi}\int_{0}^{2\pi} (u(a + r\cos(\theta),b + r\sin(\theta))-M) d\theta $$ 

The integrand is always less than or equal to zero and continuous, so we conclude that it is identically zero for all $$\theta$$.
This argument can be applied for any radius $$r < r'$$, so we conclude $$B_r(a,b)\subseteq E$$.
This means that $$E$$ is open.
Since $$E$$ is both open and closed and non-empty, it is a union of connected components of $$\Omega$$.
Since $$\Omega$$ is connected, it follows that $$\Omega = E$$.  Thus $$u$$ is constant on $$\Omega$$.
:black_square_button:



