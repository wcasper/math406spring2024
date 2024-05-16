---
layout: page
title: Final Exam Takehome Portion
permalink: /exams/final-takehome
---

### Directions
Solve the following problems and write up your solutions and submit them all together as a *single* PDF.
This portion of the exam is open book and open notes, including the online course notes.
Calculators are also fine.
However, discussing problems with others or using other online resouces is prohibited.


**Problem 1:**

Find the solution of the heat equation on a disk of radius $$R$$

$$u_t = k(u_{xx} + u_{yy}),$$

with the Dirichlet boundary condition

$$u(R,\theta,t) = B$$

and the initial condition 

$$u(r,\theta,0) = 0,\quad 0 \leq r < R,\ \ 0 \leq \theta < 2\pi.$$

Hint: your answer will use the eigenfunctions of the Laplacian on the unit disk.

**Problem 2:**

Consider the upper-half disk

$$\Omega = \{(r,\theta): 0 \leq r < R,\ \ 0 < \theta < \pi\}.$$

Find a function which is continous in a neighborhood of the closure of $$\Omega$$, harmonic inside $$\Omega$$, and satisfies the boundary conditions

$$u(r,0) = 0, \ \ u(r,\pi) = 0,\ \ u(R,\theta) = (\theta/\pi)(1-\theta/\pi)$$

on the boundary of $$\Omega$$.

Hint: use separation of variables on the Laplacian expressed in polar coordinates.

**Problem 3:**

Let $$c>0$$ and $$\gamma \geq 0 $$ be constants.

Use the substitution $$u = e^{-\gamma t/2}v$$ to find a d'Alembert-style solution of the differential equation

$$u_{tt} + \gamma u_t = c^2u_{xx}$$

on the whole real line with the initial condition

$$u(x,0) = f(x),\ \ \ u_t(x,0) = g(x).$$

:warning: Important note: by **d'Alembrt-style**, we mean an equation of the form

$$u(x,t) = \int_{\mathbb{R}} \Phi(x-x',t)f(x')dx' + \int_{\mathbb{R}} \Psi(x-x',t)g(x')dx',$$

for some functions (or more generally *distributions*) $$\Phi(x,t)$$ and $$\Psi(x,t)$$.
When $$\Phi = \frac{1}{2}(\delta_{ct}(x) + \delta_{-ct}(x))$$ and $$\Psi(x,t) = \frac{1}{2c} 1_{(-ct,ct)}(x)$$, this would give the usual d'Alembert formula.

Hint: after doing the substitution, take the Fourier transform with respect to $$x$$ to get a second order differential equation of the form

$$\hat u_{tt} + \left(4\pi^2c^2\xi^2 - \frac{\gamma^2}{4}\right)\hat u.$$

Solve this differential equation using the initial condition

$$\hat u(\xi,0) = \hat f(\xi),\ \ \  \hat u_t(\xi,0) = \hat g(\xi).$$

Then take the inverse Fourier transform back again to obtain an equation for $$u(x,t)$$ in terms of convolutions.

You can use (without proof) the fact that

$$\int_{\mathbb{R}}\frac{1}{\sqrt{4\pi^2c^2\xi^2-\frac{\gamma^2}{4}}}\sin(t\sqrt{4\pi^2c^2\xi^2-\frac{\gamma^2}{4}})e^{2\pi i\xi x}d\xi = \frac{1}{4\pi c}J_0\left(i\frac{\gamma}{2}\sqrt{t^2-\frac{x^2}{c^2}}\right)$$






