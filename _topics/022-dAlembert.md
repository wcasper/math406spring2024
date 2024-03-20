---
layout: page
title: d'Alembert's Formula
---

To solve the one-dimensional wave equation 

$$u_{tt} = c^2u_{xx},\ \ \ t>0,\ x\in \mathbb{R}$$

on the whole real line, with the boudary conditions

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

$$u(x,t) = \frac{f(x-ct)+f(x+ct)}{2} + \frac{1}{2c} \int_{x+ct}^{x-ct}g(s) ds.$$

To summarize, we have the following theorem

**Theorem (d'Alebert's Formula):**
To solve the one-dimensional wave equation 

$$u_{tt} = c^2u_{xx},\ \ \ t>0,\ x\in \mathbb{R}$$

on the whole real line, with the boudary conditions
$$u(x,0) = f(x),\ \ u_t(x,0) = g(x)\ \ x\in\mathbb{R}$$
is given by

$$u(x,t) = \frac{f(x-ct)+f(x+ct)}{2} + \frac{1}{2c} \int_{x+ct}^{x-ct}g(s) ds.$$


