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

* (a) Show that if $$u(\rho,\theta,\phi) = R(\rho)\Theta(\theta)\Phi(\phi)$$ is an eigenfunction (in spherical coordinates) with eigenvalue $$\lambda^2$$, ie. 

$$\Delta u + \lambda^2 u = 0$$

then there exist constants $$\mu$$ and $$\nu$$ with

$$\begin{align}
\rho^2R''(\rho) + 2\rho R'(\rho) + (\lambda^2\rho^2 - \mu)R(\rho) &= 0,\\
\Theta''(\theta) + \nu\Theta(\theta) &= 0,\\
\sin^2(\phi)\Phi''(\phi) + \sin(\phi)\cos(\phi) \Phi'(\phi) + (\sin^2(\phi)\mu-\nu)\Phi(\phi) &= 0.
\end{align}$$

Hint: use separation of variables for the Laplacian in spherical coordinates

$$\Delta u = u_{\rho\rho} + \frac{2}{\rho}u_{\rho} + \frac{1}{\rho^2\sin^2\phi}u_{\theta\theta} + \frac{1}{\rho^2} u_{\phi\phi} + \frac{1}{\rho^2\tan\phi} u_\phi,$$

* (b)  Explain why $$\nu = m^2$$ for some integer $$m$$a

* (c)  Show that if we substitute $$s = \cos(\phi)$$, then $$\Phi$$ satisfies the **Legendre differential equation**

$$(1-s^2)P''(s) - 2s P'(s) + (\mu-\frac{m^2}{1-s^2})P(s) = 0.$$

Solutions of this equation are called **Legendre functions**.

# Problem 3

In order for $$u(\rho,\theta,\phi) = R(\rho)\Theta(\theta)\Phi(\phi)$$ to be an eigenfunction of the Laplacian on the unit ball, we need it to be continuous on the closed unit ball.
One particular consequence of this is that the Legendre function $$P(s)$$ from the previous problem must be continuous on $$[-1,1]$$

* (a)  Prove that if $$\mu = \ell(\ell+1)$$, then the Legendre differential equation has a solution which is a polynomial of degree $$\ell$$.  The polynomial solution is called a **generalized Legendre polynomial**.
* (b)  Prove the converse of (a) is also true: that if $$P(s)$$ is a polynomial of degree $$\ell$$, then $$\mu = \ell(\ell+1)$$.

**Remark:** It turns out that the *only* Legendre functions which are continuous on $$[-1,1]$$ are the Legendre polynomials, so $$\mu = \ell(\ell+1)$$ for some integer $$\ell$$.  The corresponding eigenfunctions of the Laplacian are referred to as **spherical harmonics**.

# Problem 4

If we perform a change of variables $$t = \lambda\rho$$, then $$R(\rho) = j_\ell(t)$$ for $$j_\ell(t)$$ a **spherical Bessel function of the first kind**, ie. a continuous funcion on $$[0,\infty)$$ which solves the differential equation

$$t^2j_\ell''(t) + 2tj_\ell'(t) + (t^2 - \ell(\ell+1))j_\ell(t) = 0.$$

* (a) Solve the differential equation in the case $$\ell=0$$ and determine the value of $$j_0(t)$$, up to a constant multiple.
* (b) Repeat your calculation in (a), but now with $$\ell=1$$
* (c) Explain why the eigenvalues of the unit ball are given by the roots of the spherical Bessel functions

:warning: The Bessel functions $$J_n$$ and the spherical bessel $$j_n$$ are related, but are not the same functions.

# Problem 5

Classify the type of each of the following second-order PDEs as parabolic, elliptic, hyperbolic, or ultrahyperbolic.

* (a) $$u_{tt} -2u_{xt} + u_{xx} + u_x = 0$$
* (b) $$5u_{tt} -4u_{xt} + u_{xx} = 0$$
* (c) $$5u_{tt} -6u_{xt} + u_{xx} + u_t = 0$$
* (d) $$u_{tt} +6u_{xt} + 4u_{yt} + 4u_{xx} + 2u_{xy} + 5u_{yy} = 0$$



