---
layout: page
title: Homework 6
permalink: /homework/hw6
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

Let $$a > 1$$.

* (a) Prove that for any real numbers $$s\neq t$$

$$\int_0^R J_a(rs/R)J_a(rt/R)rdr = \frac{R^2}{s^2-t^2}\left(sJ_a'(s)J_a(t)-tJ_a(s)J_a'(t)\right).$$

Hint: copy the proof of the Bessel orthogonality theorem in class.

* (b) Use (a) to prove that

$$\int_0^R J_a(rs^a_k/R)J_a(rs^a_k/R)rdr = \frac{R^2}{2}(J_{a+1}(s^a_k))^2.$$

Hint: take a limit and use the recurrence relation

$$(J_a(r)/r^a)' = -J_{a+1}(r)/r^a.$$


# Problem 2

Consider the problem of finding eigenfunctions of the Laplacian for the unit ball in $$\mathbb{R}^3$$

* (a) Show that if $$u(r,\theta,\phi) = R(\rho)\Theta(\theta)\Phi(\phi)$$ is an eigenfunction (in spherical coordinates) with eigenvalue $$\lambda^2$$, ie. 

$$\Delta u + \lambda^2 u = 0$$

then there exist constants $$\mu$$ and $$\nu$$ with

$$\begin{align}
\rho^2R''(\rho) + 2\rho R'(\rho) + (\lambda^2\rho^2 - \mu)R(\rho) &= 0,\\
\Theta''(\theta) + \nu^2\Theta(\theta) &= 0,\\
\sin^2(\phi)\Phi''(\phi) + \sin(\phi)\cos(\phi) \Phi'(\phi) + (\nu^2-\sin^2(\phi)\mu)\Phi(\phi) &= 0.
\end{align}$$

Hint: use separation of variables for the Laplacian in spherical coordinates

$$\Delta u = u_{\rho\rho} + \frac{2}{\rho}u_{\rho} + \frac{1}{\rho^2\sin^2\phi}u_{\theta\theta} + \frac{1}{\rho^2} u_{\phi\phi} + \frac{1}{\rho^2\tan\phi} u_\phi,$$

* (b)  Explain why $$\nu$$ must be an integer

* (c)  Show that if we substitute $$s = \cos(\phi)$$, then $$\Phi$$ satisfies the differential equation

$$(1-s^2)P''(s) - 2s P'(s) + (\mu-\frac{\nu^2}{1-s^2})\Phi(s) = 0.$$

Solutions of this equation are called **Legendre functions**.  

# Problem 3




# Problem 4

Classify the type of each of the following second-order PDEs as parabolic, elliptic, hyperbolic, or ultrahyperbolic.

* (a) $$u_{tt} -2u_{xt} + u_{xx} + u_x = 0$$
* (b) $$5u_{tt} -4u_{xt} + u_{xx} = 0$$
* (c) $$5u_{tt} -6u_{xt} + u_{xx} + u_t = 0$$
* (d) $$u_{tt} +6u_{xt} + 4u_{yt} + 4u_{xx} + 2u_{xy} + 5u_{yy} = 0$$



