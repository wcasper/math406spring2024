---
layout: page
title: Unbound Solutions
---

So far, we have looked at solutions of the heat equation where the spatial dimension is constrained to be an interval $$[0,L]$$.
However, in the real world we can certainly imagine situations where we are interested in solutions of the heat equation where the spatial dimension is unbound in this manner.
These situations typically occur when the spatial dimensions are so large that they might as well be taken to be infinite.

In this situation, there is no "boundary" (hence unbound), so our boundary value problems are replaced with **Cauchy problems**, which simply specify the initial condition.

$$u_t = ku_{xx},\ \ u(x,0) = f(x).$$

To solve the Cauchy problem, we use a new fundamental solution, called the heat kernel.

# Heat kernel

**Definition:** The one-dimensional **heat kernel** is the function

$$K(x,t) = \frac{1}{\sqrt{4\pi kt}}e^{-x^2/(4kt)}, t > 0.$$

The heat kernel itself is a solution of the heat equation for $$x\in\mathbb{R}$$ and $$t > 0$$.
Of course it's not defined for $$t=0$$, but the limit as $$t\rightarrow 0$$ of $$K(x,t)$$ does exist in a certain sense.
To see how, we need to think about certain really nice functions, called **test functions**.

**Definition:** A function $$f(x)$$ has **compact support**, if the set $$\{x: f(x)\neq 0\}$$ is closed and bounded.
A function is called **smooth** if it has derivatives of every degree at every point.  A smooth function with compact support is called a **test function**.
Sometimes, these are also called **bump functions**.

**Theorem:** If $$f(x)$$ is a test function, or more generally if there exist constants $$C,r\in\mathbb{R}$$ with $$\lvert f(x)\rvert \leq Ce^{-rx^2}$$ for all $$x\in \mathbb{R}$$ then

$$\lim_{t\rightarrow 0+}\int_{\mathbb R} K(y,t)f(x-y)dy = f(x).$$

Because of this result, physicists imagined the limit $$\lim_{t\rightarrow0+} K(x,t)$$ as a new function $$\delta(x)$$ called the **Dirac delta function** given by

$$\delta(x)=\left\lbrace \begin{array}{cc} 0, & x\neq 0\\ \infty, & x = 0\end{array}\right.$$

and with the property that

$$\int_{\mathbb{R}} f(x)\delta(x)dx = f(0).$$

Clearly this isn't a real function, but the idea can be made mathematically rigorous using the idea of disributions, which define next.

## Distributions

A **distribution** on $$\mathbb{R}$$ is a linear transformation $$\chi: C_c^(\infty}(\mathbb{R})\rightarrow \mathbb{R}$$ with the property that for any sequence of functions $$\{f_n(x)\}\in C_c^\infty(\mathbb{R})$$ with $$f_n^{(k)}(x)\rightarrow 0$$ uniformly for all $k$, we must have $$\chi(f_n)\rightarrow 0$$.
A transformation $$\chi$$ defined this way is also called a **bounded linear functional** on $$C_c^\infty(\mathbb{R})$$.

The simplest distributions are functions themselves.  Specifically, if $$f(x)$$ is an integrable function on $$\mathbb{R}$$, then 

$$ C_c^\infty(\mathbb{R})\rightarrow \mathbb{R},\ \ \varphi(x)\mapsto \int_{\mathbb R} f(x)\varphi(x)dx$$

is a distribution.  In this sense, distributions can be thought of as *generalizations* of regular functions.

**Notation:** If $$\chi$$ is a distribution, we write $$\int \varphi(x) \chi(x)dx$$ to mean $$\chi(\varphi)$$.  This notation naturally extends the idea of distributions as generalizations of functions.

The simplest examples of distributions are the **Dirac delta distribution** and it's distributional derivatives $$\delta_a(x),\delta_a'(x),\dots$$ defined by

$$\int_{\mathbb{R}} f(x)\delta_a^{(k)}(x) dx = f^{(k)}(a).$$

As a special case, we write $$\delta^{(k)}(x)$$ in place of $$\delta_0^{(k)}(x)$$.
Note that linear combinations of distributions are also disributions, so they form a vector space.

We say that a sequence of distributions $$\chi_n$$ **converges weakly** or **converges in distribution** to $$\chi$$ if for all test functions $$\varphi$$ we have

$$\lim \int_{\mathbb{R}} \varphi(x)\chi_n(x)dx = \int_{\mathbb{R}}\varphi(x)\chi(x).$$

In terms of this definition, the theorem above may be restated as the fact that in the limit as $$t\rightarrow 0+$$ the heat kernel converges weakly to the Dirac delta distribution $$\delta(x)$$.

## Solving the unbound heat equation.

**Theorem:**  Suppose that $$f(x)$$ is a piecewise continuous function and that there exist constants $$C$$ and $$r$$ with $$\lvert f(x)\rvert \leq Ce^{-rx^2}$$.  Then a solution of the Cauchy problem

$$u_t = ku_{xx},\ \ u(x,0) = f(x)$$

is given by

$$u(x,t) = \int_{\mathbb{R}} K(y,t)f(x-y)dy.$$


More generally, we can solve the Cauchy problem with a nonhomogeneous heat equation

**Theorem:**  Suppose that $$f(x)$$ is a piecewise continuous function and that there exist constants $$C$$ and $$r$$ with $$\lvert f(x)\rvert \leq Ce^{-rx^2}$$.  Then a solution of the Cauchy problem

$$u_t = ku_{xx} + \phi(x,t),\ \ u(x,0) = f(x)$$

is given by

$$u(x,t) = \int_{\mathbb{R}} K(y,t)f(x-y)dy + \int_0^t \int_{\mathbb{R}} K(y,t-s)\phi(x-y,s)dy \phi(s)ds.$$





