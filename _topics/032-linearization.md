---
layout: page
title: Linearization
---

Now we want to explore the behavior of solutions of the shallow water equations in fuller generality.

$$\begin{align}
\eta_t + ((h+\eta)u)_x + ((h+\eta)v)_y &= 0,\\
u_t + uu_x + vu_y - fv + g\eta_x &= 0,\\
v_t + uv_x + vv_y + fu + g\eta_y &= 0, 
\end{align}$$

One idea to study the behavior of solutions is to suppose that we are given a known solution

$$u(x,y,t) = u_0(x,y,t),\ \ \ v(x,y,t) = v_0(x,y,t),\ \ \ \eta(x,y,t) = \eta_0(x,y,t).$$

Which we call the **base solution**.
Now if we jostle things a bit, we would expect our solution to change, but still be pretty close to the old solution.
Mathematically, we can write this as

$$u(x,y,t) = u_0(x,y,t) + \epsilon u_1(x,y,t),\ \ \ v(x,y,t) = v_0(x,y,t) + \epsilon v_1(x,y,t),\ \ \ \eta(x,y,t) = \eta_0(x,y,t)+\epsilon\eta_1(x,y,t).$$

We call this solution the **perturbed solution**, and the functions $$\epsilon u_1$$, $$\epsilon v_1$$, and $$\epsilon \eta_1$$ the **perturbation**.
When $$\epsilon $$ is very small, we can safely ignore any terms which are multiplied by $$\epsilon^2$$ as too tiny.
Inserting this into the shallow water equations and throwing out any $$\epsilon^2$$ terms, this becomes

$$\begin{align}
\eta_{1t} + ((h+\eta_0)u_1)_x + (\eta_1u_0)_x  + ((h+\eta_0)v_1)_y + (\eta_1v_0)_y &= 0\\
u_{1t} + u_1u_{0x} + u_0u_{1x} + v_1u_{0y} + v_0u_{1y} - fv_1 + g\eta_{1x} &= 0,\\
v_{1t} + u_1v_{0x} + u_0v_{1x} + v_1v_{0y} + v_0v_{1y} + fu_1 + g\eta_{1y} &= 0.
\end{align}$$

In this setup, the functions $$u_0$$, $$v_0$$, and $$\eta_0$$ are *known* and the unknown functions are $$u_1$$, $$v_1$$, and $$\eta_1$$.
The system of partial differential equations is linear in these unknown variables!
We call this the **linearization** of the equations with respect to the base solution $$u_0$$, $$v_0$$, and $$\eta_0$$.


## Shear instability

In the case that $$f=0$$ and $$h=0$$, then

$$u(x,y,t) = u_0(y),\quad v(x,y,t) = 0,\quad \eta(x,y,t) = \eta_0$$

is a solution of the shallow water equations for any constant $$\eta_0$$ and any choice of function $$u_0(y)$$.
This kind of solution is called  **shear flow**.

The linearization around this base solution is

$$\begin{align}
\eta_{1t} + \eta_0u_{1x} + \eta_0v_{1y}     + u_0(y)\eta_{1x} &= 0,\\
u_{1t}    + u_0(y)u_{1x} + u_0'(y)v_1       + g\eta_{1x}      &= 0,\\
v_{1t}    + u_0(y)v_{1x}                    + g\eta_{1y} &= 0.
\end{align}$$

The coefficients of the PDEs in the the linearization for the shear flow are independent of $$x$$ and $$t$$.
Consequently, the Fourier transform implies that any solution should be able to be expressed as an infinite linear combination of **normal modes**, ie. functions of the form

$$u_1 = e^{ik(x-ct)} U(y),\ \ \ v_1 = e^{ik(x-ct)} V(y),\ \ \ \eta_1 = e^{ik(x-ct)} H(y).$$

Using this, we get the following system of equations for the normal modes

$$\begin{align}
ik(u_0(y)-c)H   + ik\eta_0U + \eta_0V' &= 0,\\
ik(u_0(y)-c)U   + u_0'(y)V    + ikgH      &= 0,\\
ik(u_0(y)-c)V   + gH'       &= 0.
\end{align}$$

From the above equations, we get

$$(\kappa^{-2}V')' - \left[1 + 2 \frac{k^2(u_0'(y))^2}{g\eta_0\kappa^4} + \frac{u_0''(y)}{\kappa^2(u_0(y)-c)}  \right]V = 0.$$

where here

$$\kappa^2 = k^2\left[1-\frac{1}{g\eta_0}(u_0(y)-c)^2\right].$$

This differential equation doesn't have nonsingular solutions for all possible values of $$k$$ and $$c$$.
Instead, what happens is that given a choice of $$k$$, there will be certain values of $$c$$ for which the equation has a solution, leading to **dispersion relations**.
For an arbitrary profile, this is a challenging numerical task.

Let's explore solutions of this equation in the special case that

$$u_0(y) = \left\lbrace\begin{array}{cc}\end{array}\right$$




$$(\kappa^{-2}V')' - \left[1 + 2 \frac{k^2c_0^2}{g\eta_0\kappa^4} + \frac{u_0''(y)}{\kappa^2(c_0(y)-c)}  \right]V = 0.$$











