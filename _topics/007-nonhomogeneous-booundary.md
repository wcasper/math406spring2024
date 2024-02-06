---
layout: page
title: Nonhomogeneous Boundary Conditions
---

So far, we have only learned how to solve the heat equation with homogeneous boundary conditions.
Our next step is then to consider **nonhomogeneous boundary conditions**.

The strategy we demonstrate here will be to convert a nonhomogeneous BVP to a homogeneous BVP.

# Time-independent boundaries

The simplest nonhomogeneous situation is when the boundary conditions are constant in time:

$$u_t = ku_{xx},\ \ u(0,t) = a,\ \ u(L,t) = b,\ \ u(x,0) = f(x).$$

In this case we can propose a solution of the form

$$u(x,t) = a + \frac{b-a}{L}x + v(x,t).$$

Inserting this into the original equation, we get that $$v$$ satisfies the homogeneous BVP

$$v_t = kv_{xx},\ \ v(0,t) = 0,\ \ v(L,t) = 0,\ \ v(x,0) = f(x) - a - \frac{b-a}{L}x.$$

:warning: Make sure to notice the change in the initial condition!

# Time-dependent boundaries

In general, we can try to solve a nonhomogeneous BVP with time dependent boundaries using the exact same strategy.

$$u_t = ku_{xx},\ \ u(0,t) = a(t),\ \ u(L,t) = b(t),\ \ u(x,0) = f(x).$$

As before, we propose a solution of the form

$$u(x,t) = a + \frac{b(t)-a(t)}{L}x + v(x,t).$$

However, this time when we insert this into our heat equation, we get changes both to the initial condition and to the heat equation itself:

$$v_t = kv_{xx} + \frac{b'(t)-a'(t)}{L}x,\ \ v(0,t) = 0,\ \ v(L,t) = 0,\ \ v(x,0) = f(x) - a - \frac{b(0)-a(0)}{L}x.$$

This is a homogeneous boundary condition, but for a **nonhomogeneous heat equation**.
We will next study how to solve the nonhomogeneous heat equation, but before going there it is worth formally remarking on the strategy that we can use every time:

**Strategy:** By proposing the right kind of initial solution, we can change **a homogeneous heat equation with a nonhomogeneous boundary condition** into **a nonhomogeneous heat equation with a homogeneous boundary condition**


