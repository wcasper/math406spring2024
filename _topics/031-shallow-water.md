---
layout: page
title: Shallow Water Equations
---

So far, the linear theory of second-order partial differential equations, in particular in the case of constant coefficients, has been shown to be well-understood.




The **shallow water equations** are given by

$$\begin{align}
\eta_t + ((h+\eta)u)_x + ((h+\eta)v)_y &= 0,\\
u_t + uu_x + vu_y - fv + g\eta_x &= 0,\\
v_t + uv_x + vv_y + fu + g\eta_y &= 0, 
\end{align}$$

where here
* $$u$$ and $$v$$ are the velocity of the fluid in the $$x$$ and $$y$$ directions, respectively
* $$f$$ is the Coriolis parameter, for fluids in a rotating reference frame
* $$g$$ is the gravitational acceleration
* $$h$$ is the height of the ground at position $$(x,y)$$
* $$\eta$$ is the height of the water above the ground level

## The one-dimensional setting

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
\end{align}$$

Thus

$$\frac{d}{dt}(u+2c) = gh_x\quad\text{along}\quad x'(t) = u+c.$$

Likewise, if we subtract both of the previous equations, we obtain

$$\frac{d}{dt}(u-2c) = gh_x\quad\text{along}\quad x'(t) = u-c.$$

The curves defined by $$x'(t) = u\pm c$$ are called the **positive and negative characteristic curves** and the quantities $$u\pm 2c$$ are called the **Riemannian invariants**.


### Modelling a dam break

Suppose that $$h(x) = 0$$ and that our initial profile for $$u(x,t)$$ and $$\eta(x,t)$$ is given by

$$u(x,0) = 0,\quad \eta(x,0) = \left\lbrace\begin{array}{cc}\eta_0, & x < 0\\ 0, & x \geq 0\end{array}\right.$$

We can imagine this as the initial state of water which is held by a dam positioned at $$x=0$$.
We imagine that at the initial time, the dam bursts allowing the water to flow forward.
The question we would like to try to answer is what is the height $$\eta(x,t)$$ of the water at time $$t > 0$$?

Let $$(x,t) = (x_\pm(t;x_0),t)$$ be the function describing a characteristic curve emerging from the point $$(x_0,0)$$ on the $$x$$-axis.
For $$x_0 < 0$$, we have

$$\begin{align}
u+2c = 2c_0\ \ \text{on}\ \ (x_+(t;x_0),t),\\
u-2c =-2c_0\ \ \text{on}\ \ (x_-(t;x_0),t),
\end{align}$$

where here $$c_0 = \sqrt{g\eta_0}$$.

Conversely, for $$x_0 > 0$$, we have

$$\begin{align}
u+2c = 0\ \ \text{on}\ \ (x_+(t;x_0),t),\\
u-2c = 0\ \ \text{on}\ \ (x_-(t;x_0),t).
\end{align}$$

If $$x_0,x_1 < 0$$ and $$t_1$$ is a point where $$x_+(t_1;x_0) = x_-(t_1;x_0)$$, then at that point

$$\begin{align}
u+2c = 2c_0,\\
u-2c =-2c_0.
\end{align}$$

So at that point,

$$u = 0,\ \ \ \text{and}\ \ \ c = c_0.$$

Therefore, for times when $$x_\pm(t;x_0)$$ is intersecting with the opposite characteristic curves originating from the negative $$x$$-axis, we have

$$x_\pm(t;x_0) = x_0 \pm c_0t.$$

The right-most negative curve is the one emerging from the origin itself $$x_-(t;0) = -c_0t$$, and $$x_+(t;x_0)$$ intersects with this curve at $$t = -x_0/2c_0$$.
Thus we have a natural divide of the $$x,t$$-plane into two regions:

$$\Omega_- = \{(x,t): x < -c_0t\},$$

where we have discovered our characteristic curves are lines, and

$$\Omega_+ = \{(x,t): x >  -c_0t\},$$

where we aren't sure yet what happens.

A negative curve in $$\Omega_+$$ will emerge from the positive $$x$$-axis and intersect with a positive curve from the negative $$x$$-axis at each point.
On the positive curve, $$u+2c = 2c_0$$, always and $$u-2c$$ is a constant, so both are constant!
This forces $$u$$ and $$c$$ to both be constants on the negative curve, which means that the negative curve must be a straight line.
The origin $$x_0$$ of this negative characteristic curve cannot be negative, so we must have $$x_0 = 0$$.
This gives us a *family* of negative characteristic curves originating from the origin:

$$x_-(t;0) = (u-c)t.$$

Thus at the point $$(x,t)$$, we have

$$\begin{align}
u-c &= x/t\\
u+2c &= 2c_0\\
\end{align}$$

This gives

$$\begin{align}
u &= \frac{2}{3}(x/t + c_0),\\
c &= \frac{c_0}{3}(2-x/c_0t).
\end{align}$$

In particular, this gives the following result for the height of the liquid 

$$\eta(x,t) = \left\lbrace\begin{array}{cc}
\eta_0 & x < -c_0t\\
\frac{\eta_0}{9g}(2-x/c_0t)^2 & -c_0t < x < 2c_0t
\end{array}\right.$$

Note in particular when $$x > 2c_0t$$, nothing is defined.
This just comes from the fact that water hasn't made it to that position at that time.

<video controls="" width="700" height="500" muted="" loop="" autoplay="">
<source src="python/031-dam-break.mp4" type="video/mp4">
</video>

The source code for this video can be found here
* [python source code for curve plot](python/031-dam-break.py)



