---
layout: page
title: Homework 4
permalink: /homework/hw4
---

### Directions
Solve the following problems and write up your solutions.  Your solutions should be provided in one of the following formats (in order of preference)
* typed up in $$\LaTeX$$ and submitted as a PDF on Canvas
* written legibly on blank paper, scanned into a PDF and then uploaded on Canvas
* written on ancient parchement with a quill and then flown to the instructor via owl post like in Harry Potter

If you go with the first strategy, you may wish to check out Overleaf which is a free and intuitive website for generating $$\LaTeX$$ documents online.
If you wish to use the second method and don't own a scanner at home, you can check out the numerous scanning apps available for smartphones.

You will be graded based on *completion* of all of the assigned problems, along with in-depth grading of *select* problems which will not be revealed until after the homework is graded.

**Remember:** Success in any math class is based on *practice*.  The assigned homework problems are the **bare minimum**.  You should strive to do as many problems as possible from the textbook.

# Problem 1

Determine the expression for the Laplacian operator

$$\Delta = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$$

in spherical coordinates.


# Problem 2

Find the Green's function for the Laplacian and the Poisson kernel for a sphere of radius $$R$$ centered at the origin.

# Problem 3

Find a Green's function for each of the following operators

* (a) The differential operator $$L = \partial_x^3$$ on the domain $$\Omega = (0,\infty) \subseteq \mathbb R$$
* (b) The diffusion operator $$L = \partial_t - \partial_x^2$$ on the domain $$\Omega = \{(x,t): 0 < x < L,\ \ 0 < t < \infty\}$$.


# Problem 4

An **eigenfunction of the Laplacian** on a domain $$\Omega\subseteq \mathbb{R}^n$$ is a function $$u(\vec x)$$ satisfying

$$\Delta u = \lambda u,\ \ \vec x\in\Omega$$
$$u(\vec x) = 0,\ \ \vec x\in\partial\Omega$$

If such a function exists, then the associated value $$\lambda$$ is called an eigenvalue of $$\Delta$$.

* (a) Look up and explain what Bessel functions of the first and second kind are.
* (b) Use separation of variables to find the eigenfunctions and eigenvalues of the Laplacian on the disk $$\Omega = \{(x,y): x^2+y^2 < R^2\}$$.  Your answer should involve Bessel functions.
* (c) Use (b) to find an example of a nonconstant solution of the wave equation on the disk

$$u_{tt} = c^2(u_{xx}+u_{yy}),\ \ (x,y)\in \Omega,$$
$$u(x,y,t) = 0,\ \ (x,y)\in \partial\Omega.$$

# Problem 5

Find all the three dimensional plane waves, ie. all solutions of

$$u_{tt} = c(u_{xx}+u_{yy} + u_{zz})$$

in $$\mathbb{R}^3$$ which are of the form

$$u(x,t) = f(ax+by+cz - ct)$$

for some single-variable function.



