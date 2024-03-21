---
layout: page
title: d'Alembert's Formula
---


## 1-D wave equation on a line

To solve the one-dimensional wave equation 

$$u_{tt} = c^2u_{xx},\ \ \ t>0,\ x\in \mathbb{R}$$

on the whole real line, with the initial condition

$$u(x,0) = f(x),\ \ u_t(x,0) = g(x)\ \ x\in\mathbb{R}$$

we first rewrite the wave equation as an operator equation

$$(\partial_t^2-c^2\partial_x^2)u = 0.$$

Notice we can factor the operator part of the equation as

$$(\partial_t-c\partial_x)(\partial_t+c\partial_x)u = 0.$$

If we set $$w = (\partial_t + c\partial_x)u$$, then this is a *first-order* PDE in the unknown function $$w$$:

$$w_t -cw_x = 0.$$

Using the method of characteristics, we find $$w(x,t) = h(x+ct)$$ for some differentiable function $$h$$.

This gives us the non-homogeneous first-order PDE

$$u_t + cu_x = h(x+ct).$$

Then if we let $$H(x+ct) = \frac{1}{2c}\int_0^{x+ct} h(s)ds$$ and $$u = v + H$$, then we obtain he homogeneous first-order PDE

$$v_t + cv_x = 0,$$

which we can again solve via the method of characteristics.  It gives $$v = k(x-ct)$$ for some differentiable function $$k$$ and therefore

$$u(x,t) = k(x-ct) + \frac{1}{2c}\int_0^{x+ct} h(s)ds.$$

Now applying the initial conditions 

$$k(x)+\frac{1}{2c}\int_0^x h(s)ds = f(x).$$

$$-ck'(x)+\frac{1}{2}h(x) = g(x).$$

Solving this for $$h(x)$$ and $$k(x)$$, we get

$$k'(x) = \frac{1}{2}f'(x)-\frac{1}{2c}g(x)\quad\text{and}\quad h(x) = cf'(x)+g(x).$$

Integrating to get $$k(x)$$, we find

$$u(x,t) = \int_0^{x-ct}f'(s)-\frac{1}{2c}g(s) ds + f(0) + \frac{1}{2c}\int_0^{x+ct} cf'(s) + g(s) ds.$$

Finally, combining like terms, we arrive at the formula

$$u(x,t) = \frac{f(x-ct)+f(x+ct)}{2} + \frac{1}{2c} \int_{x-ct}^{x+ct}g(s) ds.$$

To summarize, we have the following theorem

**Theorem (d'Alebert's Formula):**
Suppose that $$f\in C^2(\mathbb{R})$$ and $$g\in C^1(\mathbb{R})$$.
Then a solution of the one-dimensional wave equation 

$$u_{tt} = c^2u_{xx},\ \ \ t>0,\ x\in \mathbb{R}$$

on the whole real line, with the initial condition
$$u(x,0) = f(x),\ \ u_t(x,0) = g(x)\ \ x\in\mathbb{R}$$
is given by

$$u(x,t) = \frac{f(x-ct)+f(x+ct)}{2} + \frac{1}{2c} \int_{x-ct}^{x+ct}g(s) ds.$$


## 1-D wave equation on a half-line

The simple solution presented in d'Alembert's formula can also be used to solve the wave equation on the half-line $$\mathbb R_+ = [0,\infty)$$.
This time, the associated domain *does* have a boundary (namely $$x=0$$) and at the boundary we impose a Dirichlet boundary condition.

In other words, we will try to solve the one-dimensional wave equation 

$$u_{tt} = c^2u_{xx},\ \ \ t > 0,\ x > 0$$

on the half-line, with the boundary condition $$u(0,t) = 0$$ and the initial conditions

$$u(x,0) = f(x),\ \ u_t(x,0) = g(x)\ \ x > 0.$$

For the initial condition and the boundary conditions to be compatible, we must also require $$f(0) = g(0) = 0$$.

To solve this equation, we use the **reflection method**, wherein we extend $$f$$ and $$g$$ to odd functions on $$\mathbb{R}$$

$$
\widetilde f(x) = \left\begin{array}{cc}f(x) & x \geq 0\\ -f(-x) & x < 0\end{array}\right.
\quad\text{and}\quad
\widetilde g(x) = \left\begin{array}{cc}g(x) & x \geq 0\\ -g(-x) & x < 0\end{array}\right.
$$

Since they are odd, the solution of the wave equation $$\widetilde u(x,t)$$ with the initial condition

$$\widetilde u(x,0) = \widetilde f(x),\ \ \widetilde u_t(x,0) = \widetilde g(x)\ \ x \in\mathbb{R}$$

will also define a solution on the half-line with the desired initial and boundary condition.
By d'Alembert's formula,

$$\widetilde u(x,t) = \frac{\widetilde f(x-ct)+\widetilde f(x+ct)}{2} + \frac{1}{2c} \int_{x-ct}^{x+ct}\widetilde g(s) ds.$$

Using the piecewise-definition of $$\widetilde f$$ and $$\widetilde g$$, this gives us the following theorem.

**Theorem:**
Suppose that $$f\in C^2(\mathbb{R})$$ and $$g\in C^1(\mathbb{R})$$ with $$f(0) = g(0)$$.
Then a solution of the one-dimensional wave equation 

$$u_{tt} = c^2u_{xx},\ \ \ t>0,\ x\in \mathbb{R}$$

on the whole real line, with the initial condition
$$u(x,0) = f(x),\ \ u_t(x,0) = g(x)\ \ x\in\mathbb{R}$$
is given by

$$u(x,t) = \frac{f(x-ct)+f(\lvert x+ct \rvert)}{2} + \frac{1}{2c} \int_{\lvert x-ct \rvert }^{x+ct}g(s) ds.$$




