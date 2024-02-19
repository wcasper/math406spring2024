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
Inside $$\Omega$$, harmonic functions feature two important properties: the Mean Value Property and the Maximum Principle.

The value of a function which is harmonic in $$\Omega$$ is determined by the value of the function on the booundary $$\partial\Omega$$.
Geometrically in two dimensions, a harmonic function looks like what happens when you take a wooden box and sand down the sides unevenly, so that the height of each side is described by some function.
Then if you stretch a rubber sheet oveer the top and pull it as tight as possible, the resulting surfce is a solution of Laplace's equation with Dirichlet boundary conditions


$$u_{xx} + u_{yy} = 0,\ \ u(x,0) = f_1(x),\ \ u(x,M) = f_2(x),\ \ u(0,y) = g_1(y),\ \ u(L,y) = g_2(y).$$

<p align="center"><img width=600 src="fig/013-solution-visual.png"/></p>

In three dimensions, harmonic functions describe gravitatial fields in the empty spaces *between* massive objects like planets, or electric fields in the empty spaces away frmo the source of the electric charge.

## The Mean Value Property

Suppose that $$u$$ is a harmonic function on $$\Omega\subseteq\mathbb{R}^2$$.
The Mean Value Property says that for any circle in $$\Omega$$, if we take the average over the circle, then we get the value of $$u$$ at the center of the circle:

$$\frac{1}{2\pi}\oint_0^{2\pi} u(a + r\cos(\theta),b + r\sin(\theta)) d\theta = u(a,b).$$

In three dimensions, this generalizes to the average over the surface of a ball being equal to the value at the center of the ball.
This generalizes to $$n$$ dimensions by replacing surface with hypersurface.


