---
layout: page
title: Shallow Water Equations
---

So far, the linear theory of second-order partial differential equations, in particular in the case of constant coefficients, has been shown to be well-understood.




The **shallow water equations** are given by

$$\begin{align}
\eta_t + ((h+\eta)u)_x + ((h+\eta)v)_y &= 0,\\
u_t + uu_x + vu_y - fv + g\eta_x &= 0, 
v_t + uv_x + vv_y + fu + g\eta_y &= 0, 
\end{align}$$

where here
* $$u$$ and $$v$$ are the velocity of the fluid in the $$x$$ and $$y$$ directions, respectively
* $$f$$ is the Coriolis parameter, for fluids in a rotating reference frame
* $$g$$ is the gravitational acceleration
* $$h$$ is the height of the ground at position $$(x,y)$$
* $$\eta$$ is the height of the water above the ground level

### The one-dimensional setting

Let's consider the specific case of a non-rotating reference frame, so that $$f=0$$.
In situations where the flow is unidirectional, we can assume without loss of generality that $$v = 0$$ and that all the unknown functions take on values which are independent of $$y$$.
In this case the shallow water equations reduce to the **one-dimensional shallow water equations**.

$$\begin{align}
\eta_t + (h+\eta)u_x + u(h+\eta)_x &= 0,\\
u_t + uu_x + g(h+\eta)_x &= 0.
\end{align}$$

At this point, it's helpful to introduce a new variable $$c$$, defined by

$$c^2 = g(h+\eta).$$

As we will soon see, this value has something to do with the actual velocity of the fluid $$u(x,t)$$ at each position in space.
With this new variable in mind, the equations can be rewritten as

$$\begin{align}
2c_t + cu_x + 2uc_x &= 0,\\
u_t + uu_x + 2cc_x &= g h_x.
\end{align}$$

By adding both equations together, we get

$$\begin{align}
(u+2c)_t + (u+c)(u+2c)_x &= gh_x.
\end{align}$$


Thus if we consider the family of curves in the $$x,t$$-plane defined by $$x'(t) = u(x,t)+c(x,t)$$, then along each curve

$$\begin{align}
\frac{d}{dt}(u+2c)
& = (u+2c)_x x'(t) + (u+2c)_t\\
& = (u+2c)_x(u+c) + (u+2c)_t\\
& = gh_x
$$

Thus

$$\frac{d}{dt}(u+2c) = gh_x\quad\text{along}\quad x'(t) = u+c.$$

Likewise, if we subtract both of the previous equations, we obtain

$$\frac{d}{dt}(u-2c) = gh_x\quad\text{along}\quad x'(t) = u-c.$$









